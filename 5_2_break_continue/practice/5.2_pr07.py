# Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он увеличивал пробег на 10 % от
# пробега предыдущего дня. Определить в какой день он пробежит больше x км (натуральное число x читается из
# входного потока). Результат (искомый день) вывести на экран.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.2.8
#
# Sample Input:
# 20
# Sample Output:
# 9

x = int(input())

i = 1

distance = 10

increasing_distance = 10/100

while True:
    if distance <= x:
        distance = distance + (distance * increasing_distance)
        i += 1
    if (distance > x):
        print(i)
        break