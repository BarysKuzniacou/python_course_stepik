# На вход программе подаются три целых числа, записанных в одну строку через пробел. Необходимо прочитать 
# их и определить наименьшее среди прочитанных чисел. Наименьшее найденное значение вывести на экран.
#
# P.S. Программу реализовать следует, используя условный оператор, без использования функции min.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.2.2
#
# Sample Input:
# 8 11 -1
# Sample Output:
# -1
#
# test #2
# input: 7 3 2
# output: 2
#
# test #3
# input: -1 -11 -5
# output: -11
#
# test #4
# input: 2 2 5
# output: 2
#
# test #5
# input: 3 3 3
# output: 3

a, b, c = map(int, input().split())

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)
