"""The test functions for dictionary functions."""

from exercises.ex06.dictionary import invert
import pytest
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count


__author__: str = "730225263"


def test_invert_swap() -> None:
    """Testing to assess whether invert can swap a value and key."""
    test_swap: dict[str, str] = {'key': 'value'}
    assert invert(test_swap) == {'value': 'key'}


def test_invert_empty() -> None:
    """Testing if invert will return an empty dictionary."""
    test_empty: dict[str, str] = {}
    assert invert(test_empty) == {}


def test_invert_key_error() -> None: 
    """Testing to see if invert raises a KeyError with duplicate values."""
    with pytest.raises(KeyError):
        test_same_value: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(test_same_value)


def test_favorite_color_one() -> None:
    """Test if there is only entry in book."""
    book_one: dict[str, str] = {"Piper": "black"}
    assert favorite_color(book_one) == "black"


def test_favorite_color_tie() -> None:
    """If there is a tie, should return the first color referenced."""
    book_tie: dict[str, str] = {"Maia": "green", "Jack": "red", "Skylar": "red", "Lianna": "purple", "Ashley": "orange", "Jim": "orange"}
    assert favorite_color(book_tie) == "red"


def test_favorite_color_empty() -> None:
    """Testing if favorite_color will return an empty string given an empty dict."""
    book_empty: dict[str, str] = {}
    assert favorite_color(book_empty) == ""


def test_count_empty() -> None:
    """Testing to see if count will return empty upon given an empty list."""
    xs_empty: list[str] = list()
    assert count(xs_empty) == {}


def test_count() -> None:
    """Given a list of str, count will return a dict with the frequency of each item in the list."""
    animals: list[str] = ['cow', 'pig', 'pig', 'horse', 'cow']
    assert count(animals) == {'cow': 2, 'pig': 2, 'horse': 1}


def test_count_one() -> None:
    """Given a list with only one item, count will still work."""
    count_one: list[str] = ['zebra']
    assert count(count_one) == {'zebra': 1}