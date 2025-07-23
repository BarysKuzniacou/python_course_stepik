a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
c = []

for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)

print(c)