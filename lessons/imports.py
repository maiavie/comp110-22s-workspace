"""Examples of Importing in Python."""


from lessons import helpers
from lessons import helpers as hp


from lessons.helpers import powerful
# import names defined globally in a module


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")


if __name__ == "__main__":
    main()