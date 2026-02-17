"""Current-phase relation utilities."""

import numpy as np

def current_from_dispersion(phases, dispersions):
    """Estimate supercurrent from phase derivative of ground-state energy."""
    if len(phases) != len(dispersions):
        raise ValueError("phases and dispersions must have the same length")

    ground_state_energy = []
    for energies in dispersions:
        negative = energies[energies < 0.0]
        per_k_energy = np.sum(negative) / max(1, energies.shape[0])
        ground_state_energy.append(per_k_energy)

    return np.gradient(ground_state_energy, phases)