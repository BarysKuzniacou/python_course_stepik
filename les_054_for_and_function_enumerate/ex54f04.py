digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        print(digs[i])
        digs[i] = 0

print(digs)