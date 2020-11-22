"""
5. Task
Your code should calculate the average of first n items of a list.
"""

my_list = [10, 25, 3, 11, 88]
empty_list = []
input_value = int(input('Enter a number within a list range = '))
if 0<= input_value <= len(my_list):
    for x in range(input_value):
        empty_list.append(my_list[x])

    average = sum(empty_list)/len(empty_list)
    print('Average of first {} items is {}'.format(input_value,average))

