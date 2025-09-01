# На вход программе подается натуральное число N. Необходимо его прочитать и сгенерировать вложенный список с
# помощью list comprehension, размером N x N, где первая строка содержала бы все нули, вторая - все единицы,
# третья - все двойки и так до N-й строки. Результат вывести в виде таблицы чисел как показано в примере ниже.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.6
#
# Sample Input:
# 4
# Sample Output:
# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

N = int(input())

lst_res =[]

#for i in range(0, N):
#    lst = [1 * i for j in range(0, N)]
#    lst_res.append(lst)

#lst_res = [[1 * i for j in range(0, N)] for i in range(0, N)]

lst_res = [[i] * N for i in range(0, N)]

for i in range(0, N):
    print(*lst_res[i])