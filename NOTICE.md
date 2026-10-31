# Content and contributor tooling licenses

The textual authored gameplay definitions under `modules/`, their module and root
workspace manifests, authored catalog, generated representations and accompanying documentation are
licensed under [MIT](LICENSE). This permits use, modification and redistribution
outside Parse Hero, including commercial projects. Preserve copyright and permission
notices in copies or substantial portions, including generated distributions.

Contributors retain copyright and submit content under the same MIT terms; see
[Contributing](CONTRIBUTING.md#contribution-rights). No copyright assignment is required.

The public `ph-content.py` and `ph-content.cmd` helpers and the workflow
`.github/workflows/content.yml` are
licensed under [MIT](docs/tool-licenses/MIT.md). Preserve that license and its
copyright notice when sharing or modifying those helpers.

The pinned Windows kit uses the same MIT terms for its public scripts. Its
first-party application binaries use the [Parse Hero Content Validator License
1.0](docs/tool-licenses/VALIDATOR.md): free local/CI authoring and validation use,
including commercial content projects, and redistribution of the complete,
unmodified official kit with its notices and provenance. Its third-party
components retain their own licenses. See the kit's `LICENSE.md` and measured
`validator-kit.json` for the exact scope and notices.

The content and helper grants exclude the separate application implementation,
non-corpus game assets and branding. Third-party licenses remain separate. No trademark
rights are granted, and running the validator transfers no ownership.
