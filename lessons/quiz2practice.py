"""Practice Code Writing For Quiz 2."""


def vowels_and_threes(phrase: str) -> str:
    """Returning the vowels on a list and other values if their index is a multiple of 3."""
    new_phrase: str = ""
    i: int = 0
    while i < len(phrase):
        if i % 3 == 0: 
            new_phrase += phrase[i]
        elif phrase[i] == "a":
            new_phrase += phrase[i]
        elif phrase[i] == "e":
            new_phrase += phrase[i]
        elif phrase[i] == "i":
            new_phrase += phrase[i]
        elif phrase[i] == "o":
            new_phrase += phrase[i]
        elif phrase[i] == "u":
            new_phrase += phrase[i]
        i += 1
    return new_phrase

def average_grades(book: dict[str, list[int]]) -> dict[str, float]:
    """Avg grades."""
    final_grades: dict[str, float] = {}
    for student in book:
        final_grades[student] = average(book[student])
    return final_grades


def average(xs: list[int]) -> float:
    """Giving the average of a list of numbers."""
    combined: int = 0
    i: int = 0
    while i < len(xs):
        combined += xs[i]
        i += 1
    float(combined)
    float(i)
    combined /= i
    return combined


a: int = 3
b: int = 0
c: float

def main() -> None:
    global a
    global b
    print(fun(a,b))


def fun(a: int, b: int) -> list[int]:
    global c
    nums: list[int] = []
    if b ==0:
        while len(nums) < 4:
            c = a + b / 2 