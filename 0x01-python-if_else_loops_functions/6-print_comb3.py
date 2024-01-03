#!/usr/bin/python3
for a in range(100):
    if int(a / 10) != a % 10 and int(a / 10) < a % 10:
        print("{}{}".format(int(a / 10), a % 10), end="")
        if (a != 89):
            print(", ", end="")
print("")
