"""Kwant system definitions for a phase-biased superconducting strip."""

import math

import kwant
import numpy as np

DEFAULT_WIDTH = 20


def make_infinite_junction():
    """Build and finalize an infinite system translationally invariant along x."""
    tau_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    tau_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    tau_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)

    lat = kwant.lattice.square(norbs=2)
    syst = kwant.Builder(kwant.TranslationalSymmetry((1, 0)))

    def onsite(site, phase, mu, delta, t):
        y = site.tag[1]
        local_phase = -phase / 2.0 if y < 0 else phase / 2.0
        normal = (4.0 * t - mu) * tau_z
        pairing = delta * (
            math.cos(local_phase) * tau_x - math.sin(local_phase) * tau_y
        )
        return normal + pairing

    def hopping(_site1, _site2, t):
        return -t * tau_z

    syst[(lat(0, y) for y in range(-DEFAULT_WIDTH // 2, DEFAULT_WIDTH // 2))] = onsite
    syst[lat.neighbors()] = hopping

    return syst.finalized()
