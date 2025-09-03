# На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и с помощью list
# comprehension сформировать двумерный список lst размером N x N (квадратную таблицу чисел). Гарантируется, что из
# набора введенных чисел можно сформировать квадратную матрицу (таблицу). Полученный двумерный список отобразить
# командой:
#
# print(lst)
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.9.2
#
# Sample Input:
# 1 2 3 4 5 6 7 8 9
# Sample Output:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#lst_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst_in = list(map(int, input().split()))

N = int(len(lst_in) ** 0.5)

lst = [[lst_in[i+x] for x in range(N)] for i in range(0, len(lst_in), N)]

print(lst)