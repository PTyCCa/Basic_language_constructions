"""Implement the fizz_buzz function, which returns a string with numbers (separated by spaces) in the range from begin to end, inclusive. Wherein:

If the number is divisible by 3 without a remainder, then the word Fizz is displayed instead
If the number is evenly divisible by 5, then the word Buzz is displayed instead
If the number is divisible by both 3 and 5 without a remainder, then the word FizzBuzz is displayed instead of the number
In other cases, the number itself is added to the string
The function takes two parameters (begin and end) specifying the beginning and end of the range (inclusive). If the range is empty (in the case when begin> end), then the function returns an empty string."""  # noqa E301


def fizz_buzz(start, stop):
    result = ''
    while start <= stop:
        if result:
            result += ' '
        if start % 15 == 0:
            result += 'FizzBuzz'
        elif start % 3 == 0:
            result += 'Fizz'
        elif start % 5 == 0:
            result += 'Buzz'
        else:
            result += str(start)
        start += 1
    return result
