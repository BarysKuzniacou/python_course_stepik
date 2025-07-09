words =['python', 'java', 'c++']
word_string = ''

for i in words:
    word_string += i + ' '

print(word_string.rstrip())

words =['python', 'java', 'c++']
word_string = ''
flag = True

for i in words:
    word_string += ('' if flag else ' ') + i
    flag = False

print(word_string)

words =['python', 'java', 'c++']

print(" ".join(words))