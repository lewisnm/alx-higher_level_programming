#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
ans = add(a, b)
ans1 = sub(a, b)
ans2 = mul(a, b)
ans3 = div(a, b)
print(f"{a} + {b} = {ans}")
print(f"{a} - {b} = {ans1}")
print(f"{a} * {b} = {ans2}")
print(f"{a} / {b} = {ans3}")
