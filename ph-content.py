"""Public standard-library bootstrap; the generated entry point embeds a reviewed pin.

This file is copied into the authored repository with PIN populated. Local users
explicitly invoke it; PR and maintainer jobs bootstrap their independently pinned
kit from workflow-owned constants instead of executing candidate files.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile

PIN = {'schema_version': 1, 'platform': 'win-x64', 'url': 'https://github.com/Tethys-Games/parse-hero-content/releases/download/content-validator-d99398293acc/ph-content-win-x64.zip', 'sha256': '8cc218b73817021ed8e5105603fb20000d4d678029117ad82b97f98f6b6201af', 'bytes': 140153259, 'kit_manifest_sha256': '4843a195faac478860fb3864c06afe7847306b3bc5aea7dcf1ac41db201a352b', 'producer': 'd99398293acc64bad190376b6a40b7d858e4c112', 'producer_source_files_sha256': '3eaf7597e46e7aed99a13517edf9f227dd6382e0dede8a972267ed43e360da1a', 'prerequisites': ['Python >=3.11', 'Git for Windows'], 'first_party_publication_terms': 'LicenseRef-ParseHero-Validator-1.0', 'public_helper_license': 'MIT', 'authored_content_license': 'MIT'}
MAX_ARCHIVE = 256 * 1024 * 1024
MAX_EXTRACTED = 512 * 1024 * 1024
MAX_FILES = 4096


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def safe(path):
    for item in (path, *path.parents):
        if item.is_symlink() or item.exists() and getattr(item.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Tool cache cannot contain links/reparse points: " + str(item))


def verify_kit(root, pin):
    safe(root)
    manifest_path = root / "validator-kit.json"
    if sha(manifest_path) != pin["kit_manifest_sha256"]:
        raise ValueError("Pinned validator manifest differs; preserve cache and use a fresh cache directory")
    manifest = json.loads(manifest_path.read_bytes())
    if manifest["producer"] != pin["producer"]:
        raise ValueError("Pinned validator producer differs")
    actual = set()
    for parent, directories, files in os.walk(root):
        for name in directories + files: safe(Path(parent) / name)
        for name in files:
            path = Path(parent) / name; relative = path.relative_to(root).as_posix(); actual.add(relative)
            if len(actual) > MAX_FILES: raise ValueError("Validator kit inventory bound exceeded")
            if relative != "validator-kit.json" and sha(path) != manifest["files"].get(relative):
                raise ValueError("Validator kit integrity failure: " + relative)
    if actual != set(manifest["files"]) | {"validator-kit.json"}:
        raise ValueError("Missing or unmeasured validator kit files")
    return manifest


def obtain_kit(pin, cache, archive=None):
    if (not isinstance(pin, dict) or pin.get("platform") != "win-x64" or
            any(not isinstance(pin.get(key), str) or len(pin[key]) != length or
                any(c not in "0123456789abcdef" for c in pin[key])
                for key, length in (("sha256", 64), ("kit_manifest_sha256", 64), ("producer", 40))) or
            type(pin.get("bytes")) is not int or not 1 <= pin["bytes"] <= MAX_ARCHIVE or
            not pin.get("url", "").startswith("https://github.com/Tethys-Games/parse-hero-content/releases/download/")):
        raise ValueError("Unsupported or incomplete selected validator pin")
    cache = cache.absolute(); safe(cache); cache.mkdir(parents=True, exist_ok=True)
    destination = cache / pin["sha256"]
    if destination.exists():
        retained = destination / "archive.zip"; safe(retained)
        if retained.stat().st_size != pin["bytes"] or sha(retained) != pin["sha256"]:
            raise ValueError("Cached validator archive differs from its trusted pin")
        verify_kit(destination / "kit", pin)
        return destination / "kit"
    # An incomplete download/extraction is retained separately; never overwrite a
    # different writer's verified cache or erase evidence after a failed capture.
    staging = Path(tempfile.mkdtemp(prefix="preparing-", dir=cache))
    target = staging / "archive.zip"
    if archive is not None:
        archive = Path(archive).absolute(); safe(archive)
        if archive.stat().st_size != pin["bytes"]: raise ValueError("Selected local kit archive length differs from pin")
        shutil.copyfile(archive, target)
    else:
        deadline = time.monotonic() + 120
        with urllib.request.urlopen(pin["url"], timeout=30) as response, target.open("xb") as stream:
            size = 0
            while chunk := response.read(1024 * 1024):
                size += len(chunk)
                if size > pin["bytes"] or time.monotonic() > deadline:
                    raise ValueError("Pinned kit download exceeded its byte/time bound")
                stream.write(chunk)
    if target.stat().st_size != pin["bytes"] or sha(target) != pin["sha256"]:
        raise ValueError("Validator archive SHA-256/length does not match the selected pin")
    kit = staging / "kit"; kit.mkdir()
    with zipfile.ZipFile(target) as zipped:
        entries = zipped.infolist(); seen = set(); total = 0
        if len(entries) > MAX_FILES: raise ValueError("Validator archive file bound exceeded")
        for row in entries:
            name = row.filename; path = PurePosixPath(name); total += row.file_size
            mode = row.external_attr >> 16
            if ("\\" in name or ":" in name or path.is_absolute() or any(part in ("", ".", "..") for part in name.split("/")) or
                    name.casefold() in seen or stat.S_ISLNK(mode) or row.is_dir() or total > MAX_EXTRACTED):
                raise ValueError("Unsafe or excessive validator archive member: " + name)
            seen.add(name.casefold())
        for row in entries:
            path = kit / row.filename; path.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(row) as source, path.open("xb") as output:
                shutil.copyfileobj(source, output, 1024 * 1024)
    verify_kit(kit, pin)
    try: staging.rename(destination)
    except FileExistsError:
        # Another verified extraction won the race. Leave this recovery directory.
        verify_kit(destination / "kit", pin)
    return destination / "kit"


def main(pin=PIN):
    arguments = sys.argv[1:]
    archive = None
    if "--kit-archive" in arguments:
        index = arguments.index("--kit-archive")
        if index + 1 == len(arguments): raise ValueError("--kit-archive requires a path")
        archive = arguments[index + 1]; del arguments[index:index + 2]
    cache = Path(os.environ.get("LOCALAPPDATA", tempfile.gettempdir())) / "ParseHero/content-validator"
    kit = obtain_kit(pin, cache, archive)
    return subprocess.call([sys.executable, "-I", "-B", str(kit / "ph-content.py"), *(arguments or ["prepare"])])


if __name__ == "__main__":
    try: raise SystemExit(main())
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print("ph-content bootstrap: " + str(error), file=sys.stderr); raise SystemExit(1)
