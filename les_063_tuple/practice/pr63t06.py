# На вход программе подаются целые числа, записанные в одну строку через пробел. 
# Необходимо их прочитать и сохранить в кортеже. Затем, в кортеже найти и вывести 
# в одну строчку через пробел (по порядку) все индексы неуникальных (повторяющихся) значений.

# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.3.8

# Sample Input:
# 5 4 -3 2 4 5 10 11
# Sample Output:
# 0 1 4 5

# test #1
# input: 5 4 -3 2 4 5 10 11
# output: 0 1 4 5

# test #2
# input: 3 4 2 -1 -1 3 2 10 11 3 4
# output: 0 1 2 3 4 5 6 9 10

# test #3
# input: 1 1
# output: 0 1

t = tuple(map(int, input().split()))

for i in range(len(t)):
    if i == 0 and int(t[i]) in t[i+1:]:
        print(t.index(t[i]), end = ' ')
    elif int(t[i]) in t[i+1:] or int(t[i]) in t[:i]:
        print(t.index(t[i], i), end = ' ')

# t = tuple(input().split())
# repeat_values = tuple(i for i, v in enumerate(t) if t.count(v) > 1)
# print(*repeat_values)

# tup = tuple(input().split())
# for i, x in enumerate(tup):
#     if tup.count(x) > 1:
#         print(i, end=' ')