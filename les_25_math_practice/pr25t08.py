# В программе выполняется чтение координат (x0, y0) и (x1, y1) двух радиус-векторов:

# x0, y0, x1, y1 = map(float, input().split())
              
# Необходимо вычислить угол α = alfa между ними по формуле:

# cos(alfa) = (x0 * x1 + y0 * y1) / (sqrt(x0^2 + y0^2) * sqrt(x1^2 + y1^2))

# a = arccos(cos alfa)

# Для перевода косинуса угла в радианы используйте функцию math.acos() модуля math. Результирующий угол α переведите в градусы по формуле:

# grad_a = 180 / Pi * a

# и сохраните в переменной alpha с округлением до десятых с помощью функции round().

# P.S. На экран ничего выводить не нужно.

import math

x0, y0, x1, y1 = map(float, input().split())

# здесь продолжайте программу

cos_alpha = (x0 * x1 + y0 * y1) / (math.sqrt(x0**2 + y0**2) * math.sqrt(x1**2 + y1**2))

grad_rad = math.acos(cos_alpha)

alpha = round(180 / math.pi * grad_rad, 1)