"""The test functions for dictionary functions."""

from exercises.ex06.dictionary import invert
import pytest
from exercises.ex06.dictionary import favorite_color


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