"""Implement sort_pair, which takes a pair (a tuple of two values) and returns a pair in ascending order."""  # noqa E301


def sort_pair(pair):
    (first, second) = pair
    if first > second:
        return (second, first)
    return pair
