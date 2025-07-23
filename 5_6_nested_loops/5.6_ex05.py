M, N = list(map(int, input('Enter M and N: ').split()))

zeros = []

for i in range(M):
    zeros.append([0] * N)

print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = int(input(f'Enter element [{i}][{j}]: '))

print(zeros)