# На вход программе подаются два вещественных числа, каждое с новой строки. Необходимо их прочитать и с помощью
# тернарного условного оператора вычислить наибольшее среди них и присвоить переменной d. Полученное значение
# переменной d вывести на экран.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.3.1
#
# Sample Input:
# 5.4
# -3.8
# Sample Output:
# 5.4

value_1 = float(input())
value_2 = float(input())

d = value_1 if value_1 > value_2 else value_2

print(d)