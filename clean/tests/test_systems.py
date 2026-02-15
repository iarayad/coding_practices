"""Unit tests for simple system defaults."""

from jj_supercurrent.systems import DEFAULT_WIDTH


def test_default_width_is_positive():
    assert DEFAULT_WIDTH > 0
