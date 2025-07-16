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

# удаление всех пробелов при вводе данных
math_expr_enter = input().replace(" ", "")
#math_expr_enter = '-4 - 5 + 10'.replace(" ", "")

# нахождение всех знаков +/- и запись их в список
lst_sign = []

for i, d in enumerate(math_expr_enter):
    if d == '+':
        lst_sign.append(1)
    elif d == '-':
        lst_sign.append(-1)

# определение знака "-" у первого числа
first_sign_minus = False

if math_expr_enter[0] == '-':
    first_sign_minus = True

# замена всех плюсов на пробелы
math_expr_without_plus = math_expr_enter.replace("+", " ")

# замена всех минусов на пробелы
math_expr_without_minus = math_expr_without_plus.replace("-", " ")

# удаление первого пробела, если первое значение со знаком минус
math_exp = math_expr_without_minus.rstrip()

# запись всех значений чисел в список
numbers_lst = []
numbers_lst = list(map(int, math_exp.split()))

# присвоение знаков значениям
lst_number_with_signs = []

if first_sign_minus:
    for i, d in enumerate(numbers_lst):
        lst_number_with_signs.append(d * lst_sign[i])
else:
    lst_number_with_signs.append(numbers_lst[0])
    for i in range(len(lst_sign)):
        lst_number_with_signs.append(numbers_lst[i+1] * lst_sign[i])

# подсчет суммы чисел
sum = 0

for i, d in enumerate(lst_number_with_signs):
    sum += d

print(sum)





