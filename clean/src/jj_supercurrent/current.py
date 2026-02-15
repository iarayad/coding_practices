"""Current-phase relation utilities."""

import numpy as np
import scipy.constants as const


def current_from_dispersion(phases, dispersions):
    """Estimate supercurrent from phase derivative of ground-state energy."""
    phases = np.asarray(phases, dtype=float)

    if len(phases) != len(dispersions):
        raise ValueError("phases and dispersions must have the same length")

    ground_state_energy = []
    for energies in dispersions:
        negative = energies[energies < 0.0]
        per_k_energy = float(np.sum(negative)) / max(1, energies.shape[0])
        ground_state_energy.append(per_k_energy)

    derivative = np.gradient(np.asarray(ground_state_energy, dtype=float), phases)
    return (2.0 * const.e / const.hbar) * derivative
