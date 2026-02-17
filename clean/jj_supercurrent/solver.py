"""Numerical solvers for phase-dependent dispersion relations."""

import kwant
import numpy as np

from jj_supercurrent.systems import make_infinite_junction


def compute_dispersion_vs_phase(width, phases, momenta, params):
    """Compute E(k) for each phase value using `kwant.physics.Bands`."""
    system = make_infinite_junction(width=width)

    dispersions = []
    for phase in phases:
        bands = kwant.physics.Bands(system, params={**params, "phase": phase})
        dispersions.append(np.array([bands(k) for k in momenta]))

    return {
        "phases": phases,
        "momenta": momenta,
        "dispersions": dispersions,
    }
