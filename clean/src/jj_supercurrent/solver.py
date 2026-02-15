"""Numerical solvers for phase-dependent dispersion relations."""

import kwant
import numpy as np

from jj_supercurrent.systems import make_infinite_junction


def compute_dispersion_vs_phase(phases, momenta, mu=0.4, delta=0.2, t=1.0):
    """Compute E(k) for each phase value using `kwant.physics.Bands`."""
    system = make_infinite_junction()
    bands = kwant.physics.Bands(system)

    phases = np.asarray(phases, dtype=float)
    momenta = np.asarray(momenta, dtype=float)

    dispersions = []
    for phase in phases:
        run_params = {"phase": float(phase), "mu": mu, "delta": delta, "t": t}
        energies = [bands(k, params=run_params) for k in momenta]
        dispersions.append(np.asarray(energies, dtype=float))

    return {
        "phases": phases,
        "momenta": momenta,
        "dispersions": dispersions,
    }
