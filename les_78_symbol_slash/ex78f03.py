def polyline(a, b, /, *args, mul=0, offset=0, **kwargs):
    return (a + b + sum(args)) * mul + offset


res1 = polyline(20, 30, 40, 50, mul=2, offset=11)
res2 = polyline(0, 5)

print(res1, res2)