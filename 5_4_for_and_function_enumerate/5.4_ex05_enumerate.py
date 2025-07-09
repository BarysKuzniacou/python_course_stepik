# индекс, значение = enumerate(объект)

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        print(d)
        digs[i] = 0

print(digs)