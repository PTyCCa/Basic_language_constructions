"""In this test, you will implement a small set of functions that work with line segments in a 2D plane. The segment in our case will be encoded as a pair of pairs and look something like this: ((x1, y1), (x2, y2)) (nested pairs are the ends of the segment). You need to implement four functions:

1. is_degenerated () must return true if the segment is degenerated to a point (the beginning and the end are the same);
2. is_vertical () must return true if the line is vertical;
3. is_horizontal () must return true if the line is horizontal;
4. is_inclined () must return true if the line is inclined (not vertical or horizontal)."""  # noqa E301


def is_vertical(line):
    (x1, y1), (x2, y2) = line  # noqa: WPS414
    # ^ sometimes it is just fine to unpack such nested structures
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    (x1, y1), (x2, y2) = line  # noqa: WPS414
    return x1 != x2 and y1 == y2


def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_inclined(line):
    return not (
        is_vertical(line) or is_horizontal(line) or is_degenerated(line)
    )
