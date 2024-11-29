"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""

    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 5)
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car("Hire 1")
    assert car._odometer == 0, "Car does not set odometer correctly"

    # used to see if Car's init method sets the fuel correctly
    # this should pass (no output)
    assert car.fuel == 0, "Car does not set fuel correctly"

    # used to see if Car's fuel is passed in correctly
    # this should pass (no output)
    car = Car("Hire 2", fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly"


def phrase_sentence(phrase):
    """
    Format a phrase with a captial letter and period at the end.

    >>> phrase_sentence("hello")
    Hello.
    >>> phrase_sentence("hi, this is a test")
    Hi, this is a test.
    >>> phrase_sentence("Woah this is really cool.")
    Woah this is really cool.
    """
    formatted = phrase[0].upper() + phrase[1:]
    if not formatted.endswith("."):
        formatted += "."
    return formatted


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()
