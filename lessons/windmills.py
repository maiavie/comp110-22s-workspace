"""Windmill Power!"""

from csv import DictReader


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


def str_to_float(str_list: list[str]) -> list[float]:
    """Converting a list of strings to a list of float values."""
    result: list[float] = []
    for item in str_list:
        item = float(item)
        result.append(item)
    return result


#d ata_file: str = "../data/WindData_LaurelNE_Nov2001_DoEData.csv"
# data_table: list[dict[str, str]] = read_csv_rows(data_file)
# print(data_table)

# wind_speeds: list[float] = column_values(data_table, "Average Speed (mph)")
# print(wind_speeds)

wind_speeds: list[float] = [9.4,12.2,13,11.3,9.6,9.9,8.2,6.2,6.4,7.7,9.2,8.4,9.4,10.5,10.3,9.9,10.4,11.8,13.3,13.8,13.6,11.7,7.9,9,9.3,8.5,10.6,11,10.8,9.9,10.9,11.5,11.7,11,11.6,11.7,11,12.1,13.1,13.9,13.2,13,13.1,12.7,13.7,13.8,14.2,12.9,14.1,13.5,12.3,12.1,13,15.1,14.6,14.6,14.8,15.1,14,13.4,13.9,13.3,13.3,13,12.4,12,11.4,11.7,12.3,12.9,12,11.1,12.7,12.6,12.8,12,10.9,10.6,11.6,11.1,10.2,9.4,8.5,7.2,7.7,9,9.5,9.4,9.3,8.7,8.3,8.4,8.8,8.4,7.7,7,7.1,7.7,6.6,6,4.9,3.7,4.5,4,5.1,4.9,5,5.6,5.3,5.6,5.2,5.8,8.3,7.1,9.5,9.7,9.4,12.9,15,12.2,14.5,13.7,15.1,16.1,17,16.7,17.9,17.9,18.3,18.6,18.1,19.1,19.7,18.3,19.5,18.9,19.3,18.2,18,17.6,15.9,15.5,14.3,14.4,12.6,11.2,11,10.9,10.8,10.3,10.1,11.5,12,11.3,11.3,11.7,11.4,11.4,10.9,10.1,10.7,12.1,11.3,12.8,14,14.6,15.1,14.2,13.3,13.4,14.4,14.8,15.4,15.4,14.5,13.7,14.7,15.1,16.1,16.9,17.3,17.8,19.1,19,18,17.3,16.3,15.7,13.8,13.1,12.8,10.3,9.3,9.2,9.1,8.4,8.2,7.1,7.6,8.1,9.4,10.2,11.5,12.1,10.6,8.8,8.5,9.7,11.2,12.7,12,14,15,15.7,16.4,16.7,18.6,18.5,17.2,15.5,14.1,15.9,15.9,15.3,14.8,14.7,14.8,12.5,11.3,11.6,11.4,11.5,10.7,8,7.9,9.4,8.9,9.5,8.5,8.3,9.9,9.3,9.4,8,9.1,9.4,9.7,12.1,12.3,9,9.7,9.4,9.7,8.3,8.1,7.8,6.3,5.7,5.7,6.7,5.9,7.2,8.4,9.5,10.5,12.4,12.3,12.8,12.4,11.5,11.6,13.8,
15.7,15.2,14.5,11.7,10.7,10.8,10.7,11,11.7,10,8.2,9.5,7.9,6.8,8.7,7.8,8.2,7.9,7.9,8,8.4,8.5,7.7,8.4,8.1,7.8,8.8,10.2,10.1,9.2,9,9,8.2,8.2,8.4,7.6,7.8,7.4,7.5,8,8.6,9.1,8.4,7.7,7.8,7.6,9.7,9.8,7.5,7.7,8.6,7.9,7.7,9.5,9.8,9.9,8.8,8.3,7.1,8.2,8.3,9.3,9.6,9.8,10.8,10.9,10.7,10.6,10.1,9.6,10.8,12.2,11.8,10.5,8.7,11.4,11.5,11.3,11.7,13.3,13.8,13.3,13.7,13.3,12.7,12.2,11.3,12.7,13.6,13.5,13.6,13.2,13.2,13.5,13.6,12.8,13.1,12.9,12.7,13.1,13.6,12.5,12.2,13.2,12.6,12.7,13.3,12.4,12.1,11,9.9,8.9,8.2,6.8,5.9,4.1,2.8,1.9,1.3,1.2,2.4,3,2.1,1.7,1.5,1.4,0.9,1.3,1.3,1,2.4,2.8,2.3,2.3,6.1,6.5,6.4,6.7,6.4,7.8,8.2,9.1,10.5,10.4,9.6,10.1,8.6,10.6,10.1,9.8,11.6,10,11.2,10.7,11.6,10.5,11.5,12.3,11.7,11.5,11.6,12,12.2,13,13.4,15,15.4,16,16.9,17.1,17.5,17.6,17.3,17.3,17.2,17.2,17.2,17.7,17.6,17.3,17.1,17.2,17.1,18.6,19.3,18.5,18,18.6,19,19.1,18.4,17.8,17.4,18.1,19.6,20.5,20.5,20.2,19.7,18.6,17.8,17.9,18,19.1,17.1,16,16.3,17.5,17.4,18.5,18.9,19.1,18.5,19.8,20.8,19.7,19,18.2,18.6,19.9,20,19.2,19.1,19.3,19,19.2,19.2,19.6,19.5,19.2,19.3,20.3,20.2,19.5,19.5,19.3,18.6,18.2,18.2,17.4,18.1,17.6,18.4,19,19.8,19.8,19,19.1,18.5,19.8,18.7,18.2,18.3,17,17.6,17.8,18.6,18.1,17.7,18.6,19.7,20,20.5,19.3,20.3,20.3,20.7,20.2,21.7,22,22.6,24,22.9,24.7,22.7,
25.2,25.9,26.9,28.4,30.8,30,30.7,28.5,30.1,29.3,29,28.9,28.8,29.1,29.4,26.3,28.5,27.2,25.7,26.6,28.3,25.5,26.3,26,26.2,22.9,23.1,22,23.3,22,23.1,20.2,19,18.8,18.9,16.8,18,18.5,19.7,21.1,20.7,19.2,18.8,18.6,18.2,19.5,19,18.7,17.7,17.9,18.9,18.5,19.1,19.1,19.3,18.8,20.3,21.6,21.5,21.2,21.9,22.8,24.7,24.2,23.5,22.9,21.1,20.9,20.5,20.5,20.7,20.2,20.4,21.5,22.2,21.7,22.3,21.3,20.9,20.2,21.1,21.9,22.4,22.5,22.9,22.8,23.4,24.1,24.5,23.7,24.3,23.6,21.4,19,19.7,21.7,21.7,20.5,20.5,22,22.8,22.4,21.5,21.7,22,20.2,20.9,21,20.5,17.2,14.3,11,14.1,10.6,6.8,9.4,9.9,5.3,8.8,10.5,13,12.6,13.3,15.1,14.1,13.3,14.3,14.6,14.6,15.7,16,15.6,13.8,12.2,11.8,9.9,9,8.8,8.4,7.6,6.4,7.2,5.6,5.6,5.1,4.6,5.4,5.5,3.5,5.3,4.2,4.5,5.3,5.9,6.2,6.7,7.3,6.2,6.9,5.9,4.8,4.2,4.2,5,4.7,4.2,4.3,4.5,4.9,5.7,5.4,6.2,5.9,6.3,5.6,5.9,5.6,6.3,7.6,8,8.9,8.5,8.1,8.6,9,8.1,7.9,7.6,8.1,7.4,7.2,7.8,8.4,8.3,8.7,8.6,8.5,9.2,8.9,9.1,9.4,9.5,10,9.4,9.5,9.5,9.6,9.9,9,8.6,8.3,8.6,8.6,8.8,8.4,4.5,5.7,7.2,7,9.2,8.7,9.2,11.8,11,9.1,10.8,10.2,10,10.6,11.8,12.2,11.8,10.8,9.9,10.1,10.6,10.2,10.9,11.5,11.5,12.8,13.6,13.6,13.4,13.1,12.5,12.4,12.9,14.1,15.8,16.4,14.8,12.9,13.2,14.5,14.9,14.6,14.8,15.4,15.2,12.8,12.4,14.4,14.8,15.7,16.4,15.6,14.2,12.2,13.1,15.2,15.4,14.6,15.2,14.3,
15.1,15.8,16.3,17.2,17.9,18.1,18.4,17.1,16.8,18.4,19,18.4,18.4,19.5,19.8,20.1,18.2,16.9,15.9,16.4,16,15.9,14,13.8,15.3,13.2,13.4,14.2,15.6,15.7,15.3,16.4,16.4,15.7,16.3,17.8,16.6,14.9,13.9,32.2,31,27.7,26.2,24.1,23.9,25.6,28,26.9,26.6,24.9,21.6,22.5,23.2,24.8,28.3,29.5,28.2,27.4,27.2,23.7,23.7,29.9,35.4,34.1,30.6,29.4,29.9,33,31.2,28.5,30.2,30.8,32.1,33.9,29.3,27.5,32.5,31.2,31,29.5,32.1,37,34,28.3,33.2,31.3,32.7,34.3,33.4,31.6,31,32,31.7,32.5,35.4,30.9,34.3,32.7,31.2,34.5,32.5,33.8,27.5,26.9,25.9,32.1,32.6,34.9,30.9,26.9,29.4,25.7,31.2,28.4,29.2,26.8,28.3,30.7,28.3,25.8,22.9,21.7,24.3,21.3,21.7,27.6,24.8,23.7,21.4,19.3,20,20.4,21.4,22.3,22.2,23.5,23.9,23.4,24.6,24.9,22.6,19.9,22.3,22,22.2,24.1,22.5,20.6,21,21.6,18.9,17.5,16.6,18.1,17.2,17,16.9,17.2,16.7,16.8,14.9,13.5,15.2,12.4,13,13.5,13.3,13.9,13.2,14.6,13.8,13.2,14.4,14,13.3,11.7,11.5,12.2,14.2,11.7,13.2,12.2,9.8,9.1,9.2,9.1,8.2,8.8,8.1,7.6,9.6,8.1,7.7,7.3,7.8,8.3,11,11.6,13.5,12.1,12.8,13.2,13.7,14.6,15,14.1,13.9,14.7,14.7,14.1,15.5,15.2,15.6,15.8,15.6,16.4,17.6,19.7,19.7,19.5,18.8,18.6,18.6,18.1,17.4,19.5,21.2,19,18.9,21,21.7,21.5,21.2,21.3,22.8,22.3,22.5,22.2,21.7,20.8,19.7,21.3,22.6,21.8,21.5,19.9,19,20.6,22.1,22.1,20.6,20.7,19.3,21.2,21.8,21.9,22.8,19.9,17.4,
15.8,17.3,19.2,19.9,23.1,22.1,21.3,21.7,20.8,20,19.5,18.4,17.7,19.1,18.3,19.7,18.9,18.7,19.5,19.7,19,18.7,15.8,17.1,17.1,14.7,11.8,15.7,16.7,16.9,22,19.3,19.1,17.2,16.8,18.3,16.7,14.6,14.9,15.5,15.5,18.8,19.1,18.5,20.1,20.5,22,20.3,21.8,24.5,27,28.4,25.7,23.8,24.7,26.7,27.1,26.9,26,26.1,24.8,23.8,25.3,24.5,22.3,22.9,21.9,20.2,20.6,20.2,20.2,21.2,22.5,21.2,21.6,22.2,22.3,21.2,21.6,22.1,23.4,24.3,26,26.8,27.9,29.5,27.2,27,28.2,29.9,29.8,27.7,25.5,25.4,22.9,20.4,22,19.6,22.2,23.4,22.8,22.4,22.4,21.9,19.7,18.4,14,13.8,6.4,13.6,8.6,9.6,12.1,12.8,13.3,14,14.2,14.3,12.6,12,12.5,12.7,13.5,13.6,12.8,13.9,13.6,16,15.9,12.8,12.8,13.3,13.3,13.4,14.1,15.5,15.5,15.2,15.4,14.8,14.4,15.1,14.8,14.5,14.2,13.7,13.6,13.4,14.1,14.6,13.6,13.1,12.4,11.6,11.9,11.4,12.8,13,13.7,14.3,14.6,13.2,12.4,11.5,11.1,10.8,10.2,11,11,10.6,9.8,10.1,9.2,8.3,8.2,7.6,6.3,5.3,5.6,7.4,8.7,8.7,7.2,8,6.9,6.4,6.9,6.9,6,6.6,7.6,8.3,9.2,8.5,6.9,8.6,9.4,7.2,6.8,9.1,9.4,8,8.2,9.3,8.8,8.3,7.5,6.2,6,6.7,7.3,6.2,6,5.3,7.1,6.9,5.8,6.3,6.2,5.5,5.1,5.3,5,4.9,3.6,2.7,1.2,0.9,0.8,2.7,2,1.9,2.4,2,1.5,1.8,1.7,1.4,1,0,1,2.4,2,3.2,4.8,5.9,6.8,8,7.5,6.3,5.1,7.1,8.1,8.6,8.3,10.8,11.7,12.5,13.3,13.3,15.4,15.1,14.8,14.8,15,13.5,11.6,11.2,11.4,11.2,12,14.2,13.7,12.4,11.6,12.7,12.9,
13.2,12.2,12.3,12.7,13,12.3,12,11.6,12.5,13.9,14.2,15.4,17.6,17,16.3,16.4,15.3,14.6,15.5,17.4,17.5,18.9,18.7,17.9,17.5,17,16.2,17.4,17.5,16.8,16.7,15.4,14.2,13,12,12.3,13.7,13.8,16.3,17.2,19,19.5,18.9,18.6,19.6,21.1,21.8,19.8,17.9,17.4,18.5,18.4,17.2,18.2,20,18.4,19.1,20.1,18,19.4,18.3,15.6,18.6,18.2,17.8,19.7,18.1,17.6,18.1,17.5,19.5,17,18.7,18.5,19.4,19.5,17.4,17.6,17,16.5,16.8,15.8,14.6,14.9,14.4,14.9,15.7,15.7,15.2,15.9,15.3,14.9,16.9,16.8,17.5,19.8,20.5,19.2,17.9,16.7,14.9,16.8,17.8,17.4,18.6,18.1,17.1,17.5,18.1,18.7,16.7,17,17.9,18.4,16.6,17.5,17.2,17.2,17.4,17.7,15.6,14.3,14.3,14.8,15.6,16.8,16.4,16.4,16.4,15.6,14.8,14.4,16,16.2,16.9,16.9,17.2,17.7,16.8,16.2,16.1,14.9,13.9,14.8,15.1,16,14.8,14.9,14.7,14.2,14.4,12,12.6,13.1,13.7,12.5,12.5,11.5,11.2,11.7,11.5,14.1,15,14.8,13.5,12.2,12.4,12.4,10.5,9.5,9.5,11.1,10.6,11.9,13.9,17.1,18.7,18.7,19.2,19,19.2,20.6,20.9,21,22.9,23.9,25.5,26.1,26,26.6,25.4,24,23.6,23.3,22.8,22.5,22.7,24.4,25.6,25,25.4,27.4,25.2,25.7,26.7,26.4,27.3,26.7,27.2,26.6,26.9,25.4,26.3,27.5,28.7,29.7,28.3,27,29.6,26.2,24.4,21.4,23.8,22.3,24.6,21.6,21,17.6,17.1,17.5,14.8,14.3,13.4,12.7,13,12.3,13.3,16,17.9,16.6,21.2,22.5,21.8,21.9,20.1,18.1,17.2,16.6,15.6,15.1,13.1,12.1,11.9,11.9,12.1,12.7,12.8,14.4,
15.9,16.4,16.8,17.1,17.9,17.7,17.1,15.3,13.6,12.8,12.9,14.6,17.3,20,20.5,21.2,21,21,21.3,21,20.1,19.1,18.3,17.5,16.4,15.7,15.3,16.4,17.5,17.4,16.4,16.2,15.9,14.8,13.7,13.8,14.4,13.4,14.1,14.1,14.8,14.3,14.1,14.8,17.2,19.5,19.2,18.1,19.1,18.9,16.7,15.6,16.8,15.4,13.4,11.2,10,9.7,10.4,10.5,9.4,9.4,8.7,7.7,7.2,7.9,9.1,9.4,10.6,12.1,14.6,15.8,14.6,15.9,17.1,15.8,19.5,17.9,17.2,18.5,17.9,19,20.7,22.3,21.7,21.3,24.1,23.3,23.3,21.6,23.3,23.5,21.3,22.3,19.8,21.5,20,21.1,23.5,20.5,20.5,20,23,22.5,19,22,23.3,20.6,20,21.3,20,18.2,18.2,16.9,17.9,17,20.9,20.6,20.9,19,20.1,18.1,18.3,17.9,21.5,21,19.9,20.8,20.9,19.2,19.5,21.6,19.5,17.6,18.6,18.5,18.6,19.9,19.7,18.7,18.1,18.7,18.3,19,18.6,18.5,15.6,17.1,17.5,16.2,15.4,16,16.1,16,17.2,17.8,18.1,18.7,18.3,17.8,17.2,16.4,14.9,14.5,14.1,14.3,15.4,16.2,15.6,15.5,15.2,14.8,14.6,16.6,17.1,17.5,16.6,17,14.8,13.3,14,14.6,15.3,15.3,14.7,17.1,17.4,17.7,16.3,14.8,13.9,15.3,17.4,18.5,18.1,16,15.5,14.7,14.9,12.2,9.8,9.9,11.1,11.6,10.5,10.6,9.9,9.9,11.8,11.3,9.6,11.9,15.6,14.3,14.3,14.9,15,16,14,14.4,13.2,13.7,13.5,13.6,17.5,18.1,19.5,17.2,15.8,15.5,17.5,18.9,18.6,17.3,17.2,17.6,19,18.5,19.2,18.4,16.2,17.9,18.3,17.1,16.8,16.4,17.2,16.7,16.5,16.5,14.6,13.2,14.6,12.3,12.6,12.2,10.6,10.6,11.6,12.7,
12.3,11.6,12,12.3,11.6,11.8,10.5,9.4,10.7,10.6,12.8,11.6,10.4,7.3,8.2,8.8,9.8,11.7,12.1,10.9,11.5,10.7,7.9,6.1,8.9,10.6,11.2,11.2,9.7,7.2,8.8,9.9,8.8,7.3,10.2,12.7,13.3,15.6,15.9,15.6,16,12.9,12.5,12.8,13.9,14.6,12.1,8.8,10.1,7.9,7.4,5.1,7.5,8.7,10.1,12.4,12,10.6,12.7,12,11.5,13.3,13.2,13.1,11.1,11.8,12.4,13.3,13.5,13,13,10.4,9.7,10.9,12.2,10.6,12.1,11.6,12.1,12.4,12.4,11.3,11.2,10.1,10.4,10.4,11.3,12.1,10.2,10,11.3,11.3,11.7,8.1,7.4,8.3,10.7,12,12.1,9.1,9.5,11.4,8.9,9.5,9.4,11,10.3,8.1,7.9,7.6,7.8,7.7,6.6,5.4,4.8,6,6.3,9.8,9.1,9.9,9.5,9.6,9.1,8.4,9,6.8,6,7.2,8.6,8.5,8.1,7.9,8.7,9,8,7.7,7.9,7.2,7.1,6.3,6.1,5,5.8,5.9,5.9,6.5,6,4.9,4.2,4.4,5.9,6.7,5.8,7.6,8.7,8.2,8.5,11.4,13.7,13.1,10.3,9.2,12.8,15.2,14.4,13.8,12.2,10.8,10.8,12.1,11.9,11.1,11,14.3,16.3,16.9,17.4,17.7,16.4,17.5,16.7,16,15.1,15.5,16.8,16.8,16.5,16.1,16.1,15.3,17.4,17.7,18.2,17.9,17.2,17.2,16.7,17.6,17.6,18,17.6,15.7,14.1,13.7,11.2,12.3,13.5,15.6,16.5,14.9,12.2,13.7,15.4,15.2,14,12.9,13,12,8.4,7,9.1,11.2,9.2,7.2,8.5,11.1,11.4,11.7,11.8,13.3,12.4,13.1,11.8,10.9,10.5,10.2,9.9,10.7,11.3,11.4,12,11,10.6,11,11.6,11.2,11.3,13.2,13,15.6,16.9,17.9,18.1,18.4,18.3,18.6,17.7,19.5,20.1,19.3,21.8,23,19.9,21.6,24.3,24.5,23.6,24.7,23.2,23.9,24.1,22.3,21.8,23.3,22.3,23.5,
20.7,22.5,21.5,21.2,20.6,21.4,20.1,16.3,16.3,17.9,16.6,16.5,14.9,14.1,14.9,15.6,15.7,17,17,16.8,16.8,17,15.3,16.3,16.6,17.2,17.3,16.3,16.8,17.2,17.1,18.1,17.9,17.7,17.5,16.4,17.5,18.7,19.3,18.4,19.4,19.7,19.1,18.9,18.7,18.6,17.8,17.1,17.4,17.1,16.4,17,17.5,18.6,18.4,16.6,15,16.7,18.3,17.8,19.1,20,18.9,18.9,19,17.8,15.4,14.1,14.5,16.2,16,15,16.1,17.7,17.8,17.3,18.1,17.9,17.5,18.3,18.1,16.7,16.7,15.7,14.3,14,15.2,14.7,14.3,14.7,14.9,15.4,15.1,16.9,18.3,17.6,17.4,15.7,15.9,17.6,17,18.2,18.5,16.4,16.9,16.4,16.5,17.6,18.4,18.1,18.2,18.2,18.5,17.9,17.8,17.2,18.1,18.8,20.2,20.1,19.9,22.1,21.1,21.3,20.7,26.3,28.4,29.3,28.8,31.2,29.9,27.8,28.8,27.2,23.4,22.9,23,25,25.7,28.6,27.1,24.8,23.1,22.8,21.3,18.6,19.2,18.5,18.2,16.2,17.4,19.1,20.2,20.2,20.1,20,20.5,19.3,19.8,20.1,19,18.6,19,19.1,20,21.1,20.5,17.8,16.8,17.1,16.7,16.3,17.6,15.5,14.8,16.5,19.4,20.8,21.6,23.5,25.3,25.1,22.4,22.5,22,22.2,22.8,23.5,23.4,23.9,23.9,22,20.3,19.7,18.3,19,18.3,17.6,16.7,18.2,18.8,19.9,20.7,22.2,22.6,22.1,21.1,21.5,22.4,21.5,22,22,22.4,23.3,25.4,28.9,25.9,26.7,20.4,17.4,18,17.9,16.7,17.7,19.5,20.2,21,19,17.1,17.4,17.7,17.5,19.7,20,19.3,18.3,18.6,19.3,19.7,19.3,18,16.8,17.9,19.8,18.1,18.3,16.8,18.5,19.2,20.3,20.6,21.2,20.2,22.9,22.4,20.7,21.3,24.5,20.9,
21,23,21.6,22.5,26,25.3,24.1,22.8,24.3,24.7,26.4,27.7,26.2,26.9,28,25,22.6,25.2,24.9,27.6,27.2,27.6,27.5,25.1,25.4,26.2,29.2,27.9,27.2,31.4,33.1,31.3,27.5,23.9,20.7,19.1,19.7,19.3,20.3,21.6,22.4,22.5,29.3,27.9,29.4,30.2,28.5,29.9,26.5,26.8,25.6,23.7,23.7,24.7,25.4,26.1,28.5,27.6,27,32.1,35.2,30.9,25.8,31.5,27.9,23.7,20.2,20.8,22.1,21.5,24.2,24,27.5,25.4,23.9,22.6,21.9,23.5,23.8,25,23.4,24.3,26.8,24.6,23.5,22.6,21.4,21.4,21.5,21.8,21.8,22.5,22,22.3,20.1,21.1,19.8,19.2,19.1,18.8,17.8,16.9,15.8,14.1,17.2,18.2,18.9,19.2,19.3,20.5,20.3,21.7,20.2,20.2,20,18.7,19.4,18.7,18.1,17.6,17.9,18.5,18.6,21.6,21,20.1,20.8,19,19.3,18.2,17.1,17.7,18.9,19.1,19.9,20,21.6,20.7,20.5,19.7,19.6,19,18.9,20,18.8,20,18.6,19.5,19.1,20.2,19.5,19.1,19.1,18.1,17.8,18.4,18.8,18.6,19.7,19.8,20.1,20.4,19.2,19,19,18.9,19.2,17.9,17.2,17.1,16.4,16.8,15.6,17,16.5,13.7,16.4,14.5,12.6,13.6,11.9,10.7,10.9,8.2,7.6,10.1,8.1,8.5,9.5,8.8,8.5,8.3,7.5,7.5,6.1,6.1,6.6,5,5.4,5.1,3.9,3.1,3.2,5.1,6.9,7.5,7.4,7.1,5.6,4.9,2.9,5.1,7.4,5.6,6.8,10.2,11.3,11.3,11,11.7,11.4,9.4,7.2,8.1,7.6,7.6,7.9,7.4,7.1,7.9,8.4,9.3,10.6,12,13.3,13.5,11.9,12.3,13.9,15.6,16.6,18,17.8,15.9,15.4,12.4,10.8,11.4,9.9,10.3,10.8,10.7,11.9,12.7,13.8,14.6,13.8,11.5,11.9,11.9,16.8,19.3,21.2,19.7,19.9,18.7,
18.1,18.4,18.7,19.6,18.2,17.7,18.7,17.5,18.4,19.3,20.3,18.3,19.5,18.5,18.3,15.3,18,19.6,16.9,19.2,18.6,19.7,21.2,22.3,25,24.4,23.6,24.8,23.1,21.1,22.5,22.1,23.8,25.7,25.6,26.6,25.7,26.6,25.2,24.7,25.2,24.4,25.4,24.9,25.1,21.6,24.6,24.4,23.2,22.9,20.6,20,22.1,23.4,21.2,18.5,17.6,16.1,14.1,15.3,15.8,15.6,15.8,17.1,15.9,12.5,10.3,10,10.4,8.5,8.3,9,9.3,8.2,7,8.2,9.2,10.4,13.9,13.1,13.3,14.9,14.1,13.6,12.6,13.3,12.3,9.7,12.9,11.3,10.7,12.5,11.4,10.9,12.3,12,14.5,13.8,14,12.7,10.2,13.1,13.4,9.3,12,10.2,10.9,11.3,12.8,14,15.2,9.9,8.7,9.7,11.2,11.8,13.6,14.7,15.4,16,14.9,14.4,14.1,11.6,11.2,11.7,13.1,10,9.3,12.2,13.2,10.3,13.7,13.4,13.5,14.8,15.8,14.5,15.1,11.3,11.4,10,8.2,8.9,9.2,9.5,9.2,8.5,5.4,8.3,10.4,7.3,6.3,4.6,3.5,3.6,2.3,1.5,1.6,1.5,1,2,1.3,2,1.4,2.8,2.5,2.5,2.2,1.5,2.1,2.2,2.4,1.9,3.2,2,7,7.7,7.7,8.9,9.4,10.2,8.8,8.6,9,9.9,9.9,9.7,9.8,9.2,8.6,9.1,9.8,9.7,10.2,9.3,9.4,10.1,10.4,11.5,12,12.1,13.7,13.3,14.9,15.7,17,16.1,15.8,14,15.4,17.2,16.7,16.3,16.4,16.5,16.9,17.7,18.2,17.7,13.5,15.9,17.2,16.8,16.1,18.5,18.4,18.6,17.8,18,16.6,16.2,17.6,18.1,19.2,20.6,20.3,20.2,19.1,17.4,18.2,18.9,19,19.5,19.3,18.8,20.7,20.1,19.4,16.9,14.6,13.5,13,14,17.3,18,16.8,16.7,16.2,16.9,17,15.8,15.5,14.9,14.1,14.8,14.1,14.5,17.5,10.1,13.2,16.7,
15.6,18.2,19.5,17.9,17.5,19.6,18.5,17.9,18.5,18.3,19.7,19.4,19.8,20.7,19.8,18,11.9,9.9,7.4,7.1,8.2,15.3,17.9,18.9,19.2,16.5,12,13.3,13.2,11.4,11.2,10.7,12.1,12.6,12.8,14.1,15.6,15.5,12.8,12.3,11.3,12,12.4,10.9,11.4,12.4,11.6,9.8,10.8,10.7,14.4,11.4,10.9,12.9,11.8,14.3,12.2,13.7,12,12.9,12.1,10.7,10.7,12.3,9.7,8.5,6.1,9,8.1,7.7,4.7,5.6,7.5,6.2,6.6,7.7,7.3,7.1,6,7.3,6.1,6.3,5.8,5.6,4.3,2.7,3.5,5,4.6,5.7,4.9,3.8,4.4,6.1,5.7,4.8,4.8,6.3,7.6,9,9.5,11.6,12.9,13.2,10.4,9.6,12.3,12.4,12.8,12.8,11.5,12.4,11.9,10.7,12.1,11.6,10.4,10.7,10.3,8.4,6,6.2,7.8,8.5,9.4,11.3,10.8,10.5,11,10.5,9.7,9.1,10,11.4,11,10.6,10.5,10.2,10.1,10.7,10.7,10.5,9.5,9.2,10.3,10.2,10.8,13,13,11.9,11.4,11.6,12,12.1,12.9,12.4,12.3,12.2,11.6,11.3,11,12.1,11.5,10.8,10.1,10.7,12,11.3,9.8,11,11.3,8.6,9.6,9.1,10.6,10.8,10.4,10,9.9,10.6,11.4,11.8,11.6,13.1,11.8,12.7,12.7,13.9,13.2,10.9,13.2,16.1,14,14.5,14.1,13.5,14.9,14.5,14.5,16,15.6,16.3,16.6,18.6,18.9,19,19.1,18.9,19.5,21.2,19.1,19.2,18.3,15.4,9.4,7.8,14.9,17.1,19.4,18.8,19.7,19.3,16.6,16.4,18.6,17.9,16.3,16.5,15.9,16.8,16.3,17.5,19.3,15.8,15.5,14.4,14.8,16,16.7,17.2,15.4,14.2,13,11.5,9.8,10.6,10.8,11.5,12.2,11,10.6,10.3,9.5,8.9,7.3,7,5.6,4.9,4.3,5.4,4.9,1.9,1.4,2.1,1.5,4,5.1,5.4,4.9,6.3,7.3,7.6,7.9,8.6,8.9,
7.5,8.2,10.2,10.2,11.6,10.4,8.7,7.7,6.8,6,5.9,6.6,8.3,8.7,7.9,6.1,7,9.1,10.2,11.4,12.2,14.1,17.1,16.5,17.5,16.3,17.4,16.8,17.9,19.2,18.4,18.5,23,24.6,25.5,25.1,28.3,27.3,29.2,27.4,27.2,24.8,20.2,20.7,23,27.7,30.4,31.6,31.2,34.7,33.1,35.4,33.4,37,35.7,35.9,35.6,36.4,35.7,34.8,37.1,37.4,36.8,38.4,37.7,38.4,36.3,38.2,39.2,38.3,39.2,37.8,38.5,39,35.6,35.7,37.5,36,37.5,37.6,38.4,39.1,38.7,40.2,39.8,38.8,36.8,38.2,34.6,35.2,37,36,37.2,37,41.7,38.3,36.2,40.3,39.2,37.7,39.4,37.2,35.3,35.2,33.9,39.2,34.6,34.8,33.2,37,37.2,33.6,36.6,37.7,33.3,36.3,36.6,35.4,37.3,36.5,31.4,32,33.2,32.3,37.5,36.9,31.8,33.3,37,33.1,32.4,36.7,33.1,29.1,28.6,29.7,26.8,29.6,28.1,30.3,28.3,29.1,29.3,30.6,28.1,27.8,27.1,27.7,24.3,26.2,22.1,22.4,19.4,20,22.7,21.9,25.6,21.4,24.4,27.1,25.2,22.4,23.8,25.9,23.5,22.9,21.7,21.8,22,22.2,19.8,16,16,15.3,17.2,17.8,16.9,16.8,17.2,18,17.5,17.3,16.1,14.4,18.5,16.2,14.8,15.2,13,14.8,13.6,16.1,16.7,14.5,14.5,13.2,13.6,12.8,13.9,12.9,11.1,7.2,8.8,8.4,7.7,7,7.2,7.5,8,7.6,8.9,8.9,7.5,8.5,6.7,6.6,7.7,8.4,8,7.6,7.1,6.5,5.9,6.8,5,7.1,8.3,9.1,11.9,12.7,13,11.3,13.4,14.8,15.2,16.8,15.4,15,15,14.8,13,14.7,15.1,15.4,16.2,16.1,17.2,14.4,13.7,13.7,12,13.6,12.2,13.6,11.7,13,12.7,13.3,13,14,14.1,14.7,14,13.6,14.4,15.5,16.2,16.7,17.2,
16.7,17.6,18.4,20,19.8,20.1,21.6,22.3,21.6,22.8,23.2,24.7,23.2,24.4,20,18,12.5,3.6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6.8,11.7,11,13.3,14.7,19.6,21,18.9,19,18.1,17.3,17.6,16.7,16.9,18.9,18.4,16.3,13.9,12.4,13,16.1,20,18.4,19.7,22.4,23.7,24.5,25.5,24.6,24.5,23.7,24.6,26.3,25.6,25.3,26.2,26.3,27.4,25.6,26.7,27,25.4,24.9,25.4,28.5,30.7,31.6,33,30.9,30.9,29.8,31.8,31.7,32,33.9,30.9,33.3,30.3,31.5,32.4,33.3,33.1,34.7,33.4,34.9,34.1,35.2,33.8,31.6,30.9,33.2,32.5,30.8,30.9,31.7,34.1,33.9,32.3,33.1,33.1,31.9,33.3,34.2,31.7,32.5,31,30.5,31,30.4,29.9,30.2,30.7,30.1,31.7,29.4,29,29.2,28.8,29.7,29,29,29.2,29.4,30,30.2,30.1,29.4,26.9,27.4,28,27.5,28.9,28.1,27.9,27.1,29.4,28.5,28.2,27.6,28.8,29.5,29.7,28.5,32,30.1,30.3,30.1,28.5,28,29.4,28.7,31.2,29.8,29.3,28.6,29.2,26.7,27.6,26.2,29,28.7,27.4,27.2,29,27.6,26.9,26.1,25.5,24.2,25,24.2,25.9,26.4,26,23.2,23.9,23.5,24.9,23.5,24.9,23.8,22.4,25.4,23,22.4,22.3,22.8,24.7,21.8,21.7,22.3,20.8,21,20.2,19.2,21.7,19.9,21.2,20.8,18.2,20.5,20.6,19.4,19.7,19.2,20.4,19.4,19.6,18.4,19,20.4,19.9,20.7,18.2,20.3,19.3,18.6,17.8,18.8,17.9,18.1,18,19.1,18.3,19.2,16.8,19,18.6,18.2,17.1,16.7,18.2,
17.7,15.9,17.4,17.1,18.2,19.5,19.3,17.9,17.6,16.4,19.2,17.1,19,17.2,18.2,19.7,20.3,19.4,18.2,17.6,17.8,17.5,17.1,16.2,15.9,15.6,14.7,13.3,14.3,14.3,12.9,13.3,12.9,12.7,11.7,12.6,12.1,12.4,11.8,11.2,10.5,11.2,11.3,10.7,11.9,13.2,11.8,14,15.3,16.3,15.8,16,14.9,17.5,16.1,15.9,16.7,16.7,17.3,17.2,15.9,14.8,14.7,14,12.1,13,13.4,12.7,11.6,12.3,11.8,12.3,13.3,13.3,13.9,14,14.9,13,12.8,13.1,14.6,13.8,12.1,13.6,14.4,14.4,12.9,13.6,13.5,15.6,12.6,12.8,11.4,11.7,12.7,11.7,10.5,12,11.4,10.5,10.5,10.8,10,9.9,9.7,9.8,10.1,9.7,10.4,10,8.7,9.3,9.8,10.4,10.5,8.4,8.9,8.5,7.6,7.4,4.9,5.1,4.7,6.8,6.4,5.2,4.8,5,5,5.4,6.5,7,5.3,5.7,6.1,5.6,6,5.8,5.2,3.7,3.6,4.6,5.2,5.6,5.9,6.2,6.7,6.6,8,8.2,7.8,7.4,8.1,7.5,6.7,5.5,5.1,3.1,2.2,2.1,0.9,0,0,0,1,2.7,3,3.7,6.1,7.2,6.4,6.4,6.2,5.5,5.1,6.1,8.7,8.7,9.2,8,7.8,7.8,7,7.6,8.1,8.5,7.2,6.5,6.9,6.5,7.8,8.4,8.9,10.7,9.8,9.5,10.7,10.9,11.4,12.1,12,10.9,11.2,11.6,12.2,12.7,14.5,15.1,17.6,16.4,14.9,15.9,17.9,17.8,18.7,18.8,20.4,20.3,20.7,21.6,20.2,17.8,18.5,17.4,18.2,18.1,19.3,19.5,17.9,18.7,16.4,16.2,12.7,14.3,13.8,15.5,12.8,11.8,9.8,8.7,10.9,13.6,13,12,16.7,15.5,16.3,20.6,19.3,19.8,17.2,19.1,16,17.9,15.8,16.4,16.9,17,15.4,13.9,13.6,15.8,17.3,15.9,17.7,16.4,14.8,13.7,16.5,16.1,15.2,15.7,16.6,16.6,15.3,15.1,
15.5,15.8,14.6,13,14.6,16.2,14.8,14.6,14.6,14.6,13.8,14.2,13.6,13.2,15.8,14.7,14.1,12.9,13.9,12.8,12.8,12.8,10.1,10.7,11,11.4,11.6,11.4,11.7,12.8,13.2,12.4,12.1,10.6,12,11.5,12.2,12.4,12.9,14.4,15.1,15.6,17.1,18.1,17,18.8,18.9,17.7,17.1,17.5,18.8,17.8,17.2,17.2,20.3,19.1,19.9,19.8,20.6,21.1,19,16.7,18.7,17.5,17.9,16.3,18.3,17.2,17.9,16.3,16.7,20.6,17.7,17.1,15.9,15.2,14.4,15.4,16.6,15.8,17.1,16.3,15.5,15.6,14.3,13.9,13.7,13.8,14.8,14.3,13.3,14.8,17,16.3,15.6,14.9,12.3,11.3,14.6,16.7,15.6,17.2,17.5,17.6,16.6,18.2,16.4,12.7,14.5,14.5,14.9,15.4,14.7,14.3,13.3,13.3,13,12.2,12.6,12.4,11.8,10.9,10.7,11,11.2,13.6,12.1,12,14,13.3,12.3,12.5,11.5,10.7,10.2,11.9,9.3,9.8,9.4,10.1,10.9,11.4,12.3,12.8,13.5,12.9,12.4,13.1,13.1,12.9,13.3,12.6,11.1,10.6,9.5,11,12.9,11.8,10.9,11.8,13.3,12.9,11,12.7,11.7,11.8,13.3,12,13.3,13.9,16.3,13.7,11.6,11.9,13.3,12.7,13.5,14,11,11.5,10,9.7,12.1,11.2,8.9,8.8,8.9,9.5,8.6,9,11.1,11.3,7.5,10.6,11.5,11.4,10.6,8.8,9.2,10.3,9.9,11.3,10.7,12.1,13.2,12.9,9.6,9.8,12.4,9.1,6.9,8.2,8.5,8.3,7.5,6.2,7.2,7,7.9,5.8,6.4,8.4,10.6,10.4,9.4,8.7,9.1,9.1,10.5,12.3,12.1,12.5,14.4,15.2,15.5,14.6,13.6,12.8,12.8,12.5,11.7,10.7,11.5,13.4,13.6,13.8,13.9,13.8,14.2,15.2,15.4,16.3,16.4,17.1,17.8,17.3,18.3,18.6,17,17.9,19.1,17.7,
18.6,19.3,20.2,19.7,19,17.7,17,17.2,17.2,17.9,17.8,17.1,17,19.7,22.2,22.1,21.3,20.7,19.1,19.3,16.6,14.9,17,16.5,16,16,15.4,12,10.2,12.7,14.5,15.3,15.5,16.7,17.8,17.5,18.3,18.3,18.1,18.5,18.5,18.1,18.9,19.2,17.1,16.3,16.7,18.3,17.7,19.8,19.3,19.2,18.8,18.7,18.5,19.2,19.2,18.7,18.4,18.1,18.5,18.6,18.1,17,16,15.5,14,14.3,16.4,18.8,19,19.1,22.8,23,22,22.2,23.2,24.1,25.3,24.5,23.7,24.3,24.1,23.7,22.2,23.5,22.7,22.5,22.4,22.9,22.6,23.9,24.4]


def wind_power(wind_speeds: list[float]) -> float:
    """Calculating total electrical power output from windmills."""
    result: float = 0.0
    for value in wind_speeds:
        if value < 3.5:
            result += 0.0
        if value >= 3.5 and value <= 14:
            result += (3817.7 * value ** 3)
        if value >= 14 and value <= 25:
            result += 59635775.4
        if value > 25:
            result += 0.0
    return result

print(wind_power(wind_speeds))