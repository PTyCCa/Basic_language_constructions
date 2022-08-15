from challenges.segments_classification import (
                                                is_degenerated,
                                                is_horizontal,
                                                is_inclined,
                                                is_vertical,
)

VERTICAL = (15, 5), (15, -5)
HORIZONTAL = (5, 15), (-5, 15)
DEGENERATED = (42, 100), (42, 100)
INCLINED = (0, 0), (1, 1)


def test_is_vertical():
    assert is_vertical(VERTICAL)
    assert not is_vertical(HORIZONTAL)
    assert not is_vertical(DEGENERATED)
    assert not is_vertical(INCLINED)


def test_is_horizontal():
    assert not is_horizontal(VERTICAL)
    assert is_horizontal(HORIZONTAL)
    assert not is_horizontal(DEGENERATED)
    assert not is_horizontal(INCLINED)


def test_is_degenerated():
    assert not is_degenerated(VERTICAL)
    assert not is_degenerated(HORIZONTAL)
    assert is_degenerated(DEGENERATED)
    assert not is_degenerated(INCLINED)


def test_is_inclined():
    assert not is_inclined(VERTICAL)
    assert not is_inclined(HORIZONTAL)
    assert not is_inclined(DEGENERATED)
    assert is_inclined(INCLINED)
