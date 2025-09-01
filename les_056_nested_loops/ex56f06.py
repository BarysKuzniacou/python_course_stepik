A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 ,11 ,12], [13, 14, 15, 16]]

for r in A:
    for c in r:
        print(c, end = '\t')
    print()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

print('new')

for r in A:
    for c in r:
        print(c, end = '\t')
    print()
