def triangle(a, b, c, /, mul, offset=0):
    return (a + b + c) * mul + offset


res1 = triangle(10, 20, 30, 1)
res2 = triangle(10, 20, 30, mul=2)
res3 = triangle(10, 20, 30, offset=10, mul=2)

print(res1, res2, res3)