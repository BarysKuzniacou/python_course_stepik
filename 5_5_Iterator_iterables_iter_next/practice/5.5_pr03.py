# На вход программе подается строка. Нужно ее прочитать и создать итератор для перебора символов этой строки.
# Затем, через созданный итератор перебрать все символы до первого пробела. В процессе перебора символы выводить на
# экран в одну строчку друг за другом (без пробелов). Гарантируется, что во введенной строке имеется хотя бы
# один пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.5.3
#
# Sample Input:
# Возможно-это будет полезно
# Sample Output:
# Возможно-это
from math import trunc

phrase = input()

it = iter(phrase)

flag = True

index_empty = phrase.index(' ')

for i in range(index_empty):
    print(next(it), end = '')