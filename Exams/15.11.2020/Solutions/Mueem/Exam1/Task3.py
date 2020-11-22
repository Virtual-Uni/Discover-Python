"""
3. Task:
Given a number, n, write a program that for all non-negative integers i < n, print * in separate
line.
"""

input_value = int(input('Enter a positive number = '))

if 1<=input_value<=50:
    if input_value == 0:
        print('please enter a positive number, not 0 ')

    for i in range(0, input_value):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

else:
    print('out of range')
