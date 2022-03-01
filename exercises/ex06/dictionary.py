"""Dictionary Exercise."""

__author__: str = "730225263"


def invert(first: dict[str, str]) -> dict[str, str]:
    """Given the dictionary first, invert will swap its keys and values."""
    i: int = 0
    doubles: list[str] = []
    for key in first:
        doubles.append(first[key])
    while i < len(first) - 1:
        if doubles[i] == doubles[i + 1]:
            raise KeyError("Sorry, you have at least one duplicate value. Try again!")
        i += 1
    swapped: dict[str, str]
    swapped = dict()
    for key in first:
        swapped[first[key]] = key
    return swapped


def favorite_color(book: dict[str, str]) -> str:
    """Selecting the most popular color from a dict of favorites."""
    fave: str = ""
    colors: list[str] = list()
    for key in book:
        colors.append(book[key])
    frequency: dict[str, int] = dict()
    i: int = 0
    while i < len(colors):
        frequency[colors[i]] = times(colors, colors[i])
        i += 1 
    n: int = 0
    if len(colors) > 0:
        fave = colors[n]
    while n < len(colors) - 1:
        if frequency[colors[n]] > frequency[colors[n + 1]]:
            fave = colors[n]
        n += 1 
    return fave
    

def times(seq: list[str], a: str) -> int:
    """Identifying the number of times an item appears in a list."""
    instance: int = 0
    c: int = 0
    while c < len(seq):
        if a == seq[c]:
            instance += 1
        c += 1
    return instance


# def count(xs: list[str]) -> dict[str, int]:
    """Will yield the number of times an item appears in a list."""
