"""In this test, you will work with "triples" - tuples of three elements. You have to implement two functions that "rotate" the triple left and right. How it looks like, you can understand from a couple of examples:"""  # noqa E301


def rotate_left(triple):
    elem1, elem2, elem3 = triple
    return (elem2, elem3, elem1)


def rotate_right(triple):
    elem1, elem2, elem3 = triple
    return (elem3, elem1, elem2)


def rotate_left_ver2(triple):
    return triple[1:] + triple[:1]


def rotate_right_ver2(triple):
    return triple[-1:] + triple[:2]
