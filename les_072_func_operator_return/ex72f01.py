def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res


a = get_sqrt(49)

print(a)