# На вход программе подается натуральное число n. Необходимо его прочитать и найти все простые числа (нацело делятся
# только на 1 и на себя), которые меньше числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку
# через пробел.
#
# Ликбез: квадратная скобка - граница включается; круглая скобка - граница исключается. Например [2; n) - диапазон
# от 2 до n-1 целых чисел.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.3
#
# Sample Input:
# 11
# Sample Output:
# 2 3 5 7
from sys import prefix

n = int(input())
lst_res = []


for i in range(2, n):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        lst_res.append(i)

print(*lst_res)