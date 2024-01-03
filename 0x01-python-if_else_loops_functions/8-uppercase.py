#!/usr/bin/python3
def uppercase(str):
    for g in range(len(str)):
        if ord(str[g]) >= 97 and ord(str[g]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[g]) - letter), end='')
    print()
