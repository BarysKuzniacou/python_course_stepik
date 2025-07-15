# На вход программе подается строка, в которой записано арифметическое выражение. Например:
# "10 + 25 - 12"
# или
# "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть произвольным.
#
# Необходимо прочитать эту строку из входного потока и выполнить вычисление, записанного в ней арифметического
# выражения. Результат вычисления отобразить на экране.
from sys import prefix

# Полагается, что в качестве арифметических операций используется только сложение (+) и вычитание (-), а в качестве
# операндов только целые числа. Следует учесть, что математические операции могут быть записаны как с пробелами (до
# и после), так и без них.
#
# P.S. В целях обучения программу следует делать без использования функции eval.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.3
#
# Sample Input:
# 10+25 - 12
# Sample Output:
# 23

#math_expr = input().replace(" ", "")
math_expr = '10+25 - 12'.replace(" ", "")

# находим все знаки +/-
lst_oper = []

for i, d in enumerate(math_expr):
    if d == '+':
        lst_oper.append(1)
    elif d == '-':
        lst_oper.append(-1)

print(lst_oper)

# определяем есть ли знак - у первого числа

first_sign_minus = False

if math_expr[0] == '-':
    first_sign_minus = True

math_expr_1 = math_expr.replace("+", " ")
math_expr_2 = math_expr_1.replace("-", " ")

print(math_expr_2)

numbers_lst = int(math_expr_2.split())

print(numbers_lst)

sum = 0

lst = []

if first_sign_minus:
    for i, d in enumerate(math_expr_2):
        lst[i] = int(math_expr_2[i]) * lst_oper[i]
else:
    for j in len(math_expr_2):
        if j == 0:
            lst[j] = int(math_expr_2[j])
        else:
            lst[i] = int(math_expr_2[i]) * lst_oper[i-1]

print(lst)




