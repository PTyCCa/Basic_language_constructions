from challenges.palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome('rotor')
    assert is_palindrome('abba')
    assert is_palindrome('r')
    assert is_palindrome('')


def test_not_is_palindrome():
    assert not is_palindrome('motor')
    assert not is_palindrome('bulb')
    assert not is_palindrome('blablab')
