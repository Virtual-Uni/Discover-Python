"""
6. Task
Your code should calculate the average mark of students in a dictionary as key/value pairs.
Key represents the name of the student, whereas value represents marks_list from last few exams.
"""

marks_dictionary = {
'Hasan': [10, 5, 20],
'Sakir': [10, 10, 14],
'Hanif': [20, 15, 10],
'Saiful': [20, 20, 20]
}
empty_list = []
for x in marks_dictionary.keys():
    empty_list.append(x)
for y in empty_list:
   marks_list = marks_dictionary[y]
   average = sum(marks_list) / len(marks_list)
   print('Average of {} : {}'.format(y,average))

