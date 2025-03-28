print("-9 abs = ", abs(-9)) # abs() - вычисление модуля числа
print("9 abs = ", abs(9))

print("2 , 17, 99, -3, 57, -108, 79 min:", min(2 , 17, 99, -3, 57, -108, 79)) # min
print("2 , 17, 99, -3, 57, -108, 79 min:", max(2 , 17, 99, -3, 57, -108, 79)) # max

print("3^2 =", pow(3, 2)) # возведение в степень

print("3.256789 round =", round(3.256789, 2)) # round() - округление числа
print("3.225 round =", round(3.225, 2)) # если 5 - после запятной округляются четные в сторону нечетных
print("3.235 round =", round(3.235, 2))
print("3.245 round =", round(3.245, 2))
print("3.255 round =", round(3.255, 2))
print("3.265 round =", round(3.265, 2))
print("3.275 round =", round(3.275, 2))
print("3.285 round =", round(3.285, 2))
print("3.295 round =", round(3.295, 2))
print("0.5 round =", round(0.5)) # если 5 - нечетные числа округляются в сторону четных
print("1.5 round =", round(1.5))
print("2.5 round =", round(2.5))
print("3.5 round =", round(3.5))
print("4.5 round =", round(4.5))
print("5.5 round =", round(5.5))
print("6.5 round =", round(6.5))
print("0.2 round =", round(0.2))
print("0.7 round =", round(0.7))
print("1.3 round =", round(1.3))
print("1.8 round =", round(1.8))
print("876.256789 округление до 10-ов =", round(876.256789, -1)) # округление до 10-ков
print("876.256789 округление до 100-н =", round(876.256789, -2)) # округление до 100-тен

import math

print("sin -1:", round(math.sin(-1), 2))
print("sin -0.5:", round(math.sin(-0.5), 2))
print("sin 0:", round(math.sin(0), 2))
print("sin 0.5:", round(math.sin(0.5), 2))
print("sin 1:", round(math.sin(1), 2))

print("округление до наибольшего целого 5.2:", math.ceil(5.2)) # ceil()
print("округление до наименьшего целого 5.2:", math.floor(5.2)) # floor()

print("факториал 6:", math.factorial(6)) # factorial()

print("отбрасывание дробной части 5.2345:", math.trunc(5.2345)) # trunc()

print(math.log2(4)) # логарифм
print(math.log(27))
print(math.log(27, 3))

print(math.sqrt(49)) # квадратный корень

print(math.pi)

print(math.e)




