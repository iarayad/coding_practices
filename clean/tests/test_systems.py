"""Unit tests for system construction."""

from jj_supercurrent.systems import make_infinite_junction


def test_make_infinite_junction_has_sites():
    system = make_infinite_junction(width=20)
    assert len(system.sites) > 0
