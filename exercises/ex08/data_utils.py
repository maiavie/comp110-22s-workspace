"""Dictionary related utility functions."""

__author__ = "730225263"

from csv import DictReader
from sys import float_info


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """To transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(initial: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in initial:
        i: int = 0
        stored: list[str] = []
        while i < n and i < len(initial):
            stored.append(initial[column][i])
            i += 1
        result[column] = stored
    return result


def select(full: dict[str, list[str]], chosen: list[str]) -> dict[str, list[str]]:
    """Making a new dict with only the columns of interest (chosen columns)."""
    result: dict[str, list[str]] = {}
    for column in chosen:
        result[column] = full[column]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]
    for column in second:
        if column in result:
            result[column] += second[column]
        else:
            result[column] = second[column]
    return result


def count(initial: list[str]) -> dict[str, int]:
    """Given a list, this function yields the number of times a unique value appeared in the input list."""
    result: dict[str, int] = {}
    for item in initial:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def convert_str(column: list[str]) -> list[int]:
    """Converting a list[str] into a list[int]"""
    new_column: list[int] = []
    for value in column:
        if value != '':
            new_column.append(int(value))
        else:
            new_column.append(4)
    return new_column


def of_these_rows(column: list[int], threshold: int) -> float:
    """Given a column, will tell us what percent answered above a certain threshold."""
    over_threshold: int = 0
    for answer in column:
        if answer >= threshold:
            over_threshold += 1
    result: float = (over_threshold / len(column)) * 100
    return result