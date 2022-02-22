"""Tests to verify the functionality of utils functions."""

__author__ = "730225263"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_negative() -> None:
    xs: list[int] = [-2]
    assert only_evens(xs) == [-2]


def test_only_evens_many() -> None:
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_odds() -> None: 
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_sub_negative_start() -> None: 
    a_list: list[int] = [1, 2, 3, 4]
    start: int = -1
    end: int = 3
    assert sub(a_list, start, end) == [1, 2, 3]


def test_sub_empty() -> None:
    a_list: list[int] = []
    start: int = 0
    end: int = 1
    assert sub(a_list, start, end) == []


def test_sub_portion() -> None: 
    a_list: list[int] = [2, 4, 6, 8, 10]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [4, 6, 8]


def test_concat_empty() -> None:
    xs: list[int] = []
    ys: list[int] = [8, 6, 7, 5, 3, 0, 9]
    assert concat(xs, ys) == [8, 6, 7, 5, 3, 0, 9]


def test_concat_combine() -> None:
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_sizes() -> None:
    xs: list[int] = [-3, -4, 6, 9, 10, 12]
    ys: list[int] = [1, 100]
    assert concat(xs, ys) == [-3, -4, 6, 9, 10, 12, 1, 100]

