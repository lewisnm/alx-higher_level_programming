#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        naks = number % 10
    else:
        naks = number % -10
        naks *= -1

    print("{:d}".format(naks), end='')
    return (naks)
