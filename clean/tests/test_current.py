"""Unit tests for current-phase relation utilities."""

import numpy as np
import pytest

from jj_supercurrent.current import current_from_dispersion


def test_current_shape_matches_phases():
    phases = np.linspace(0.0, 2.0 * np.pi, 9)
    dispersions = [np.array([[-0.2 + 0.02 * i, 0.2 - 0.02 * i]]) for i in range(9)]

    current = current_from_dispersion(phases, dispersions)

    assert current.shape == phases.shape


def test_current_raises_on_length_mismatch():
    phases = np.linspace(0.0, 2.0 * np.pi, 5)
    dispersions = [np.array([[-0.1, 0.1]])] * 4

    with pytest.raises(ValueError, match="same length"):
        current_from_dispersion(phases, dispersions)
