"""Kwant system definitions for a phase-biased superconducting strip."""

import kwant
import numpy as np

tau_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
tau_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
tau_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
tau_0 = np.eye(2)
sigma_0 = np.eye(2)
sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)


def make_infinite_junction(width):
    """Build and finalize an infinite system translationally invariant along x."""
    lat = kwant.lattice.square(norbs=4)
    syst = kwant.Builder(kwant.TranslationalSymmetry((1, 0)))

    def onsite(site, phase, mu, delta, t, zeeman_x, zeeman_y, zeeman_z):
        y = site.tag[1]
        local_phase = -phase / 2.0 if y < 0 else phase / 2.0
        normal = (4.0 * t - mu) * np.kron(tau_z, sigma_0)
        zeeman = zeeman_x * np.kron(tau_0, sigma_x)
        zeeman += zeeman_y * np.kron(tau_0, sigma_y)
        zeeman += zeeman_z * np.kron(tau_0, sigma_z)
        pairing = delta * (
            np.cos(local_phase) * np.kron(tau_x, sigma_0)
            - np.sin(local_phase) * np.kron(tau_y, sigma_0)
        )
        return normal + zeeman + pairing

    def hopping_x(_site1, _site2, t, alpha):
        base = -t * np.kron(tau_z, sigma_0)
        rashba = 0.5j * alpha * np.kron(tau_z, sigma_y)
        return base + rashba

    def hopping_y(_site1, _site2, t, alpha):
        base = -t * np.kron(tau_z, sigma_0)
        rashba = -0.5j * alpha * np.kron(tau_z, sigma_x)
        return base + rashba

    syst[(lat(0, y) for y in range(-width // 2, width // 2))] = onsite
    syst[kwant.builder.HoppingKind((1, 0), lat, lat)] = hopping_x
    syst[kwant.builder.HoppingKind((0, 1), lat, lat)] = hopping_y

    return syst.finalized()
