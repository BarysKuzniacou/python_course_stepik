# Гражданин 1 января открыл счет в банке, вложив 1000 руб. Каждый год размер вклада увеличивается на 5% от имеющейся
# суммы. Определить сумму вклада через n лет (n - целое положительное число, читаемое из входного потока). Результат
# (сумму вклада) округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.10
#
# Sample Input:
# 5
# Sample Output:
# 1276.28

n = int(input())

deposite = 1000
ANNUAL_RATE = 0.05

i = 0

while i < n:
    deposite = deposite + (deposite * ANNUAL_RATE)
    i += 1

print(round(deposite, 2))