#!/usr/bin/pytthon3
def safe_print_list(my_list=[], x=0):
    try:
        for value in my_list[:x]:
            print(value, end='')
    except IndexError:
        print("\nIndex does not exist")
        return 0
    print()
    return len(my_list[:x])
