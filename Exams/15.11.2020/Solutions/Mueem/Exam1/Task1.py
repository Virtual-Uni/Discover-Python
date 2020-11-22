
"""
1. Task:
# Given a year, write a program that detects whether the year is leap year or not.
"""

input_year= int(input("Enter a Year, which is a number = "))
if 1<=input_year<=5000:
    if (input_year % 4) == 0:
        if (input_year % 100) == 0:
            if (input_year % 400) == 0:
                print("{0} is a leap year".format(input_year))
            else:
                print("{0} is not a leap year".format(input_year))
        else:
            print("{0} is a leap year".format(input_year))
    else:
        print("{0} is not a leap year".format(input_year))

else:
    print('out of range')