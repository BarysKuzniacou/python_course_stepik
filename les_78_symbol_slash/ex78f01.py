def triangle(a, b, c, /):
    return a + b + c


res1 = triangle(10, 20, 30)
res1 = triangle(10, c=20, b=30) # ошибка - только позиционные аргументы

print(res1, res2)