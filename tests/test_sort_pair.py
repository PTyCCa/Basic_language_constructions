from lessons.sort_pair import sort_pair


def test_sort_pair():
    assert sort_pair((5, 1)) == (1, 5)
    assert sort_pair((2, 2)) == (2, 2)
    assert sort_pair((7, 8)) == (7, 8)
