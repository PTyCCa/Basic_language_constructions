"""Implement the binary function,
which returns a binary representation
a non-negative decimal number as a string.

Algorithm
Converting Decimal to Binary
is done according to the following algorithm:

1. The original number (number) is divided in half.
2. Remainder of division (modulo)
is written to the beginning of the string (result).
3. The original number becomes the number
obtained by the formula: number // 2.
4. If the original number (number) is greater than zero,
then we repeat from the first point.
5. If the original number is zero,
then we return (result)."""


def binary(number):
    if not number:
        return '0'
    binary_number = ''
    remainder = number
    while remainder:
        bit = remainder % 2
        binary_number = str(bit) + binary_number
        remainder = remainder // 2
    return binary_number
