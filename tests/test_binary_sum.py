from challenges.binary_sum import binary_sum


def test_sum_binary():
    assert binary_sum('1000', '10') == bin(0b1000 + 0b10)[2:]
    assert binary_sum('1010', '101') == bin(0b1010 + 0b101)[2:]
    assert binary_sum('1', '1') == bin(0b1 + 0b1)[2:]
    assert binary_sum('1111', '1111') == bin(0b1111 + 0b1111)[2:]
