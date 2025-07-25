# На вход программе подаются целые числа, записанные в одну строку через пробел. Необходимо прочитать эти числа и
# сохранить в списке. Затем, каждый элемент этого списка продублировать один раз. Например, для списка:
# [1, 2, 3]
# после дублирования должны получить:
# [1, 1, 2, 2, 3, 3]
# Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.5
#
# Sample Input:
# 8 11 2
# Sample Output:
# 8 8 11 11 2 2

lst_input = list(map(int, input().split()))

lst_result = []

for i, d in enumerate(lst_input):
    lst_result.append(d)
    lst_result.append(d)

print(*lst_result)