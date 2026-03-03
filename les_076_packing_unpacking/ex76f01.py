# * - упаковка
# ** - распаковка

x, *y = (1, 2, 3, 4)

print(y) # [2, 3, 4]

*x, y = (1, 2, 3, 4)

print(x) # [1, 2, 3]

x, *y = [1, 'a', True, 4]

print(y) # ['a', True, 4]

*x, y, z = 'Hello Python!'

print(x) # ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o']
print(y) # n
print(z) # !