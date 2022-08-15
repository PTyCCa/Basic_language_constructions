from lessons.binary import binary


cases = [
    ['0', 0],
    ['1', 1],
    ['101', 5],
    ['110', 6],
    ['1011', 11],
    ['1100101', 101],
    ['100100101001', 2345],
]


def test_binary():
    for expectation, argument in cases:
        assert binary(argument) == expectation
