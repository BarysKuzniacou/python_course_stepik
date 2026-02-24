def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res, x # (res, x)


def get_max2(a, b):
    return a if a > b else b


def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))


a = get_sqrt(49)
print(a)

x, y, z = 5, 7, 10
print(get_max3(x, y, z))

