#!/usr/bin/pytthon3
def safe_print_list(my_list=[], x=0):
    try:
        for value in my_list[:x]:
            print(value, end='')
    except IndexError:
        break
    print()
    return len(my_list[:x])
