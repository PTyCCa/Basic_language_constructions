from challenges.rotate_triple import (
                                      rotate_left,
                                      rotate_right,
                                      rotate_left_ver2,
                                      rotate_right_ver2,
)

TRIPLE = (42, 'a', None)


def test_rotate_left():
    assert rotate_left(TRIPLE) == ('a', None, 42)
    assert rotate_left(rotate_left(rotate_left(TRIPLE))) == TRIPLE
    assert rotate_left_ver2(TRIPLE) == ('a', None, 42)
    assert rotate_left_ver2(rotate_left(rotate_left(TRIPLE))) == TRIPLE


def test_rotate_right():
    assert rotate_right(TRIPLE) == (None, 42, 'a')
    assert rotate_right(rotate_right(rotate_right(TRIPLE))) == TRIPLE
    assert rotate_right_ver2(TRIPLE) == (None, 42, 'a')
    assert rotate_right_ver2(
                             rotate_right_ver2(
                               rotate_right_ver2(TRIPLE))) == TRIPLE


def test_both():
    assert rotate_right(rotate_left(TRIPLE)) == TRIPLE
    assert rotate_left(rotate_right(TRIPLE)) == TRIPLE
    assert rotate_right_ver2(rotate_left_ver2(TRIPLE)) == TRIPLE
    assert rotate_left_ver2(rotate_right_ver2(TRIPLE)) == TRIPLE
