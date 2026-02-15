# Good vs Bad Coding Practices: Josephson Junction Demo

## Goal
Compare two implementations of the same task:
1. Build a Josephson junction model in Kwant.
2. Sweep superconducting phase.
3. Compute dispersion and supercurrent.

## Bad Version (`bad/josephson_messy.ipynb`)
- Everything in one notebook and one global namespace.
- Poor naming (`WTF_W`, `mkBadOne`, `BANDZZ`) and hidden side effects.
- Unnecessary typing noise in notebook functions.
- Model, numerics, plotting, and interpretation all mixed.
- Duplicated logic and magic values.
- No tests, no linting, no reproducibility workflow.

## Clean Version (`clean/`)
- Modular package structure (`systems.py`, `solver.py`, `current.py`).
- Reproducible environment and task runner via `pixi.toml`.
- Linting and formatting via Ruff + pre-commit.
- Tests via `pytest`.
- Architecture and process docs for collaboration.

## Practices from arXiv:2507.16166v1 and Where We Use Them
Source: https://arxiv.org/html/2507.16166v1

1. Plan Before You Code
- Applied in `clean/docs/architecture.md`.
- Scope, boundaries, and known limitations are written down before implementation.

2. Design for Modularity
- Applied in `clean/src/jj_supercurrent/systems.py`.
- Applied in `clean/src/jj_supercurrent/solver.py`.
- Applied in `clean/src/jj_supercurrent/current.py`.
- Applied in `clean/scripts/run_supercurrent.py`.

3. Write Clean and Readable Code
- Applied by enforcing Ruff through `clean/pyproject.toml` and `clean/.pre-commit-config.yaml`.
- Functions are small and each file has one main responsibility.

4. Use Version Control Practices
- Applied with clear repository structure and review workflow in `clean/CONTRIBUTING.md`.
- Evolution tracked in `clean/CHANGELOG.md`.

5. Test Regularly
- Applied in `clean/tests/test_current.py`.
- Applied in `clean/tests/test_systems.py`.
- Applied via `pixi run test` task in `clean/pixi.toml`.

7. Document Everything
- Applied in `clean/README.md`.
- Applied in `clean/docs/architecture.md`.
- Applied in this summary and in slides.

8. Strive for Reproducibility
- Applied in `clean/pixi.toml` (pinned Python + dependencies + tasks).
- Applied in `clean/pyproject.toml` (package and tool config).

10. Plan for Long-Term Maintenance
- Applied with lint hooks, tests, changelog, and contribution rules.

## Not Fully Implemented Yet
- No CI pipeline configured yet.
- No benchmark/performance suite yet.
- No regression test against external reference data yet.

## Takeaways
- Keep physics logic separate from orchestration.
- Keep notebooks exploratory; keep reusable logic in modules.
- Treat linting, tests, and documentation as part of scientific correctness.
- Reproducibility and maintainability are core research quality requirements.
