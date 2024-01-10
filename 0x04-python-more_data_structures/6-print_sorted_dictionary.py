#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_tuple = list(a_dictionary.items())
    sorted_items = sorted(dict_tuple)
    sorted_dict = dict(sorted_items)
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
