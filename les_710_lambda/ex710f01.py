s = lambda a, b: a + b
print(s(1, 2))

a = [4, 5, lambda: print('lambda'), 7, 8]
print(a)
a[2]()