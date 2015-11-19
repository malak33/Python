#! /usr/bin/python3
# createOrderedDict.py - below will add create an ordered Dict.py

import csv
from collections import OrderedDict

file1 = "/Users/mnobile/PycharmProjects/ClamPy/PreClass/betaTest3.txt"
"""
Follow up: you can also count the number of values you have

using

len(table_entries)
"""
# test
def read_csv_file(file_name):
    with open(file_name) as f:
        r = csv.DictReader(f)

        table_entries = []
        temp_dictionary = OrderedDict()

        for row in r:
            for key, value in row.items():
                temp_dictionary[key] = value
            table_entries.append(temp_dictionary)
            temp_dictionary = OrderedDict()
    return table_entries


def custom_logic(table_entries):
    for row in table_entries:
        for key, value in row.items():
            if key == " date_1":
                print(value)


def main():
    table_a = read_csv_file(file1)
    new_table = custom_logic(table_a)

main()