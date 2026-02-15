# Clean Josephson Junction Example

Simple package-based implementation of:
1. Kwant system definition.
2. Dispersion relation vs phase.
3. Supercurrent from phase derivative of ground-state energy.

## Run

```bash
cd clean
pixi run test
pixi run lint
pixi run run-demo
```

## Structure
- `src/jj_supercurrent/systems.py`: system definition.
- `src/jj_supercurrent/solver.py`: dispersion computation.
- `src/jj_supercurrent/current.py`: current computation.
- `scripts/run_supercurrent.py`: end-to-end script.
- `tests/`: unit tests.

## Docs
- `docs/architecture.md`: design scope and assumptions.
- `CONTRIBUTING.md`: contribution workflow.
- `CHANGELOG.md`: version history.
- `../summary.md`: consolidated good-vs-bad and paper-practices mapping.
- `../slides.md`: Quarto Revealjs presentation.

## Build Slides (Quarto)
```bash
quarto render ../slides.md
```
