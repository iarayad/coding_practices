# Repository Guidelines

## Project Structure & Module Organization
This repository currently centers on:
- `clean/`: primary package implementation (`src/jj_supercurrent`, `tests/`, `scripts/`, docs).
- `bad/`: intentionally messy notebook example (`bad/josephson_messy.ipynb`) for comparison.

Top-level teaching artifacts are `summary.md`, `slides.md`, `slides.html`, and `slides_files/`.

## Build, Test, and Development Commands
Use Pixi tasks from `clean/`:
- `cd clean && pixi run lint` checks style (`ruff check`).
- `cd clean && pixi run format` formats code (`ruff format`).
- `cd clean && pixi run test` runs unit tests (`pytest`).
- `cd clean && pixi run run-demo` runs the end-to-end script.
- `cd clean && pixi run precommit` runs all configured pre-commit hooks.

## Coding Style & Naming Conventions
- Python 3.11, 4-space indentation, and small single-purpose functions.
- Follow Ruff settings in `clean/pyproject.toml` (`line-length = 88`).
- Use `snake_case` for functions/modules/variables, `UPPER_CASE` for constants, `PascalCase` for classes.
- Keep domain terms explicit (`phase`, `mu`, `delta`, `t`) and pass physics via explicit params.

## Testing Guidelines
- Framework: `pytest` (configured in `clean/pyproject.toml`).
- Place tests in `clean/tests/`.
- Name files/functions as `test_*.py` and `test_*`.
- Before opening a PR, run `pixi run lint` and `pixi run test` in `clean/`.

## Commit & Pull Request Guidelines
- Keep commits focused and atomic; do not mix refactors and behavior changes.
- Commit messages should be short, imperative, and specific (e.g., `Refactor solver params plumbing`).
- PRs should include:
  - what changed,
  - why it changed,
  - how it was validated (exact commands run).
- Add plots/screenshots when scripts or visuals change.
