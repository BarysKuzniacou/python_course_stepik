n = int(input())

lst = [64, 32, 16, 8, 4, 2, 1]

lst_res = []

for i in lst:
    while i <= n:
        lst_res.append(i)
        n -= i

print(*lst_res)