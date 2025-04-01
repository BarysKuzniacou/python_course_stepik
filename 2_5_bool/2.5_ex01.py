print("2 > 3 :", (2 > 3))
print("5 <= 7.2 :", (5 <= 7.2))

res = 2 > 1
print(type(res))

a = 10
print(f"a = {a} четное? -", a % 2 == 0)
print(f"a = {a} нечетное? -", a % 2 != 0)
print(f"a = {a} >= 2 и <= 20? -", 2 <= a <= 20)

# and
print(f"a = {a} < 2 и > 20? -", a < 2 and a > 20)

# or
print(f"a = {a} <= 2 и >= 20? -", a < 2 or a > 20)

# not
x = 7
print(x % 2 != 0 and x % 3 != 0)
print(not (x % 2 == 0 and x % 3 == 0))

# or 3-d priority
# and 2-nd priority
# not 1-st priority (high)

# bool() - выполняет преобразование входного аргумента в логический тип True или Flase
print('bool пустое', bool())
print('bool -9', bool(-9))
print('bool 0', bool(0))
print('bool пробел', bool(' '))
print('bool ''', bool(''))