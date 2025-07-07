# На вход программе подается натуральное число n. Прочитайте это число и с помощью цикла for определите является
# ли оно простым (то есть, делится нацело только на само себя и на 1). Вывести на экран строку "ДА", если n
# простое и строку "НЕТ" в противном случае.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.3.8
#
# Sample Input:
# 11
# Sample Output:
# ДА
from sys import flags

n = int(input())

flag_1 = False
flag_2 = False
flag_3 = True

for i in range(1, n+1):
    if i == 1 and n % i == 0:
        flag_1 = True
    if i == n and n % i == 0:
        flag_2 = True
    if (i != n and n % i == 0) and (i != 1 and i != n):
        flag_3 = False
    i += 1

if (flag_1 and flag_2 and flag_3):
    print('ДА')
else:
    print('НЕТ')