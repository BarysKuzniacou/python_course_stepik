a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]

print(a)