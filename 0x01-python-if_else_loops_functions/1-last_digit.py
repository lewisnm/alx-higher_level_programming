#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigi = 0

if number > 0:
    lastdigi = number % 10
else:
    lastdigi = (abs(number) % 10) * -1

if lastdigi > 5:
    print(f"Last digit of {number} is {lastdigi} and is greater than 5")
elif lastdigi == 0:
    print(f"Last digit of {number} is {lastdigi} and is 0")
else:
    print(f"Last digit of {number} is {lastdigi} and is less than 6 and not 0")
