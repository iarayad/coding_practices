---
title: "Writing Good Scientific Code"
subtitle: "Josephson Junction Supercurrent Case Study"
author: "Group Meeting"
format:
  revealjs:
    theme: simple
    slide-number: true
    chalkboard: true
    incremental: true
    transition: slide
    center: false
---

## Motivation
- Scientific code often starts as exploration.
- Exploration code is not production/research pipeline code.
- Poor structure increases error risk and review time.

## Physics Task
1. Build BdG tight-binding model in Kwant.
2. Sweep phase difference `phi`.
3. Compute dispersion relation `E(k)` at each phase.
4. Compute current from `I(phi) = (2e/hbar) dE_GS/dphi`.

# Bad vs Clean

## Deliberately Bad Notebook
File: `bad/josephson_messy.ipynb`

- Bad names and typing noise.
- Global mutable state.
- Hidden side effects.
- Model + solver + plotting coupled in giant cells.
- No testing or reproducibility workflow.

## Clean Project Layout
Directory: `clean/`

- `src/jj_supercurrent/systems.py`: system builder.
- `src/jj_supercurrent/solver.py`: dispersion computation.
- `src/jj_supercurrent/current.py`: current extraction.
- `scripts/run_supercurrent.py`: orchestration + plotting.

## Clean Workflow
```bash
cd clean
pixi run lint
pixi run test
pixi run run-demo
```

# Practices from arXiv:2507.16166v1

## 1) Plan Before You Code
Where used:
- `clean/docs/architecture.md`

How:
- Scope, boundaries, and known limitations are explicit.

## 2) Design for Modularity
Where used:
- `clean/src/jj_supercurrent/systems.py`
- `clean/src/jj_supercurrent/solver.py`
- `clean/src/jj_supercurrent/current.py`
- `clean/scripts/run_supercurrent.py`

How:
- One module, one primary responsibility.

## 3) Write Clean and Readable Code
Where used:
- `clean/pyproject.toml`
- `clean/.pre-commit-config.yaml`

How:
- Ruff linting and formatting rules are enforced.

## 4) Use Version Control Practices
Where used:
- `clean/CONTRIBUTING.md`
- `clean/CHANGELOG.md`

How:
- Contribution process and change history are documented.

## 5) Test Regularly
Where used:
- `clean/tests/test_current.py`
- `clean/tests/test_systems.py`
- `clean/pixi.toml`

How:
- Tests are easy to run (`pixi run test`) and target core numerical logic.

## 7) Document Everything
Where used:
- `clean/README.md`
- `clean/docs/architecture.md`
- `summary.md`

How:
- Setup, assumptions, boundaries, and limitations are written down.

## 8) Strive for Reproducibility
Where used:
- `clean/pixi.toml`
- `clean/pyproject.toml`

How:
- Pinned environment and repeatable task commands.

## 10) Plan for Long-Term Maintenance
Where used:
- lint + tests + docs + changelog together

How:
- Lower style drift and safer iteration as code evolves.

## What Is Not Fully Implemented Yet
- CI pipeline
- Performance benchmark suite
- Reference-data regression tests

# Adoption

## Team Checklist
1. Keep reusable logic in modules, not notebooks.
2. Enforce lint + tests before commit.
3. Pin environment and define run commands.
4. Record assumptions and known limitations.

## Discussion
- Which part of our workflow still looks like the bad notebook?
- Which single standard should we adopt this week?
