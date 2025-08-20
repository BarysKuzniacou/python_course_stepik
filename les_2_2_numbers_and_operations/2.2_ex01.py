# типы чисел
# int float complex
# операции +, -, *, /, // - деление с округлением к наименьшему целому,
# % - остаток от деления, ** - возведение в степень

a = 2+3*3
print(a, type(a))

b = 2+3.5
print(b, type(b))

c = 8/2
print(c, type(c)) # получится вещественное число несмотря на деление целых и без остатка

d = 98/47
print(d, type(d))

e1 = 7 // 2
print(e1, type(e1)) # результат int = 3
e2 = -7 // 2
print(e2, type(e2)) # результат int = 4

f = 7 // 2.1
print(f, type(f)) # результат float

g = 5*5
print(g ,type(g)) # результат int
g = 5 * 5.1
print(g ,type(g)) # результат float

h = 10 % 3
print(h ,type(h)) # результат int
h = 9 % 5
print(h ,type(h)) # результат int = 4
h = -9 % 5
print(h ,type(h)) # результат int -9 - (-10) = 1

h = 9 % -5
print(h ,type(h)) # результат int 9 - 10 = -1

h = -9 % -5
print(h ,type(h)) # результат int - 9 % -5 = -4

i = 2 ** 3
print(i ,type(i))
i = 2 ** 3 ** 2 # возведение в степень работает справа на лево
print(i ,type(i))

j = 27 ** 1/3 # приоритет операции возведения в степень выше чем у деления
print(j ,type(j))

k = 1
k += 1
print(k)

