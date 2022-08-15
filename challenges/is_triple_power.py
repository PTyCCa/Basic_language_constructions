"""Implement the is_power_of_three () function, which determines whether the passed number is a natural power of a triple. For example, the number 27 is the third power: 3 ** 3, and 81 is the fourth: 3 ** 4."""  # noqa E301
from math import log


def is_power_of_three(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number


def is_power_of_three_ver1(some_int):
    while some_int > 0:
        return log(some_int, 3) % 1 == 0
