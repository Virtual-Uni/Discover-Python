"""
4. Task
Your provided code section should find a meaning of a word from a dictionary containing
key/value pairs of word: value.
line.
"""
input_word = input('Enter a word(Passed/Failed/Other) = ')
dictionary = {'Passed':'You have practiced at home.', 'Failed': 'You was not serious.',
'Other': 'Write your own meaning.'}

if input_word.isalpha():
    print(dictionary[input_word])

else:
    print('Enter a string')


