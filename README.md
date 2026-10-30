# Parse Hero content

This repository owns the editable M4 content. Descriptive source under `modules/`
is also the exact source served by the generated root `release.json`. Root workspace
files declare entries and references to shared modules. There is no second blob tree.

On Windows, edit source, run `ph-content.cmd prepare`, run `ph-content.cmd check`,
review `git diff`, and commit the complete tree. The convenience command verifies the
pinned validator and prepares metadata automatically. Web/fork contributors edit
source and open a PR. Protected automation opens a prepared PR if generated changes
are needed. After trusted checks and review, maintainers use GitHub's merge queue;
no local checkout or manual hash entry is required. See [Contributing](CONTRIBUTING.md)
and [Maintainers](docs/maintainers.md), including the required enforcement setup.

The selected Windows kit distribution is a versioned public GitHub Release in this
repository. Its validator-use and helper licenses are described in [NOTICE.md](NOTICE.md).
The first Windows kit is published as an immutable release; the exact URL and hashes
are in `tools/validator.json`. Active GitHub rules/runs establish workflow enablement;
compatible content/application rollout remains a separate decision. Authored
definitions and their generated representations use [MIT](LICENSE); contributors
retain copyright and submit under the same terms. Commercial reuse outside Parse Hero
is permitted. The application implementation and branding remain separately scoped.
