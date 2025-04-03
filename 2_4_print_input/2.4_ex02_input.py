a = input()
print(a, type(a))

b = float(input())
c = abs(b)
print(c, type(c))

#d = float(input("Введите длину прямоугольника: "))
#e = float(input("Введите ширину прямоугольника: "))
d, e = map(float, (input("Введите две стороны прямоугольника через пробел: ").split()))
print(f'Периметр с длиной {d} и шириной {e} равен {2 * (d + e)}' )

