# На вход программе подаются вещественные числа, записанные через пробел. Необходимо прочитать эти числа и сохранить
# в списке. Затем, все отрицательные значения в этом списке заменить на -1.0. Результат (список) выведите на экран в
# виде последовательности чисел, записанных через пробел. Программу следует реализовать с использованием функции
# enumerate.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.7
#
# Sample Input:
# -5.67 3.5 6.89 -3.0
# Sample Output:
# -1.0 3.5 6.89 -1.0

lst = list(map(float, input().split()))

for i, data in enumerate(lst):
    lst[i] = data if data >= 0 else float(-1)

print(*lst)