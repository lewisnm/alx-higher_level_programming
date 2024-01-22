#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for value in my_list[:x]:
        try:
            print("{}".format(value), end="")
        except IndexError:
            break
    print()
    return len(my_list[:x])
