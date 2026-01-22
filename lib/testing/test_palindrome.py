
#    Basic Cases – Check common inputs return expected outputs.
#    Edge Cases – Handle single-character strings, empty strings, long strings, and no-palindrome cases.
import pytest
from palindrome import longest_palindromic_substring

#Data-Driven Tests
@pytest.mark.parametrize("input, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("", ""),
    ("abcdefg", "a"), 
    ("12321", "12321"),
    ("racecar", "racecar"),
    ("noon", "noon"),
    ("abccba", "abccba"),
    ("xyzzyx", "xyzzyx"),
    ("racecarracecarracecarracecarracecarracecarracecarracecarracecarracecar", "racecarracecarracecarracecarracecarracecarracecarracecarracecarracecar"),
    ("(((()))", "(((("),
])

def test_longest_palindromic_substring(input, expected):
    assert longest_palindromic_substring(input) == expected


#Bad Data Types – Raise TypeError for non-string inputs.
@pytest.mark.parametrize("input", [
    (None),
    (12345),
    (3.14159),
    (True),
])

def test_longest_palindromic_substring_bad_data(input):
    with pytest.raises(TypeError):
        longest_palindromic_substring(input)