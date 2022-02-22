"""Exercise 5 Functions. """

__author__ = "730225263"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of integers, containing only the elements of the input list that were even."""
    i: int = 0
    evens: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(a_list: list[int], start: int, end: int) -> list[int]: 
    """Given a list and a start and ending point, creates a sub-list."""
    sub_list: list[int] = []
    if end > len(a_list) - 1:
        end = len(a_list) - 1
    if start < 0:
        start = 0
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return sub_list
    i: int = start
    while i < end:
        sub_list.append(a_list[i])
        i += 1
    return sub_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Combining two lists of integers into one list."""
    combined_list: list[int] = []
    i: int = 0
    while i < len(xs):
        combined_list.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        combined_list.append(ys[i])
        i += 1
    return combined_list
