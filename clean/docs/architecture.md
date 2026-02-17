# Architecture Notes

## Scope
This demo computes the phase-dependent supercurrent of a Josephson junction in three steps:
1. Build a Kwant infinite system.
2. Compute dispersion `E(k)` for each phase value.
3. Derive `I(phi)` from the phase derivative of a ground-state energy proxy.

## Module boundaries
- `jj_supercurrent/systems.py`: only system construction.
- `jj_supercurrent/solver.py`: only dispersion computation.
- `jj_supercurrent/current.py`: only post-processing to current.
- `scripts/run_supercurrent.py`: orchestration and plotting.

## Design constraints
- Keep APIs small and explicit.
- Keep physics assumptions local to the module that uses them.
- Prefer readability over premature optimization.

## Known limitations
- Ground-state energy is approximated from sampled band energies, so this is for teaching and workflow demonstration.
- Numerical convergence (k-grid and phase-grid sensitivity) is not fully benchmarked in this demo.
