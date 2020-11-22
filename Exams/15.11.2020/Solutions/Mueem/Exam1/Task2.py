"""
2. Task:
Given a number, n, write a program that for all non-negative integers i < n, print i2.
"""

input_value = int(input('Enter a positive number = '))
if 1 <= input_value <= 50000:
    if input_value == 0:
        print(input_value)
    for x in range(input_value):
        print(x*x)

else:
    print('out of range')


