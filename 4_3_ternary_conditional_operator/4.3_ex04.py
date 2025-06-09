a = 2
b = 3
c = -5

res = (a if a > c else c) if a > b else (b if b > c else c)

print(res)