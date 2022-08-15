"""A palindrome is a word or text that can be read equally in both directions.
Examples:
- "I am",
- "radar",
- "assa",
- "the donkey is looking for porridge at the mother-in-law"

Implement the is_palindrome () function, which takes a word as input, determines whether it is a palindrome, and returns a boolean value."""  # noqa E301


def is_palindrome(string):
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True  # or return some_string == some_string[::-1]
