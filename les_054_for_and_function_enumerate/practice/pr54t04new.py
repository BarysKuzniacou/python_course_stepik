# Необходимо написать программу формирования квадратной двумерной таблицы чисел matrix размером N x N, 
# где N - целое число (больше нуля), читаемое из входного потока командой:

# N = int(input())
                  
# Таблица matrix должна описываться двумерным вложенным списком и содержать целые числа от 1 и далее по порядку, записанных "змейкой".
# Например, для таблицы matrix размером N=5, должны получить следующий вложенный список:

# matrix = [
#     [1, 2, 3, 4, 5],
#     [16, 17, 18, 19, 6],
#     [15, 24, 25, 20, 7],
#     [14, 23, 22, 21, 8],
#     [13, 12, 11, 10, 9]
# ]

                  
# Выведите полученный список matrix на экран командой:

# for row in matrix:
#     print(' '.join(str(num) for num in row))

# N = int(input())

matrix = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]

# N = 5

# matrix = [[0] * N for n in range(N)]

# print(matrix)

# k = 1

# for i in range(N):
#     for j in range(N):
#         matrix[i][j] = k
#         k += 1

# print(matrix)

print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4])
print(matrix[1][4], matrix[2][4], matrix[3][4], matrix[4][4])
print(matrix[4][3], matrix[4][2], matrix[4][1], matrix[4][0])
print(matrix[3][0], matrix[2][0], matrix[1][0])
print(matrix[1][1], matrix[1][2], matrix[1][3])
print(matrix[2][3], matrix[3][3])
print(matrix[3][2], matrix[3][1])
print(matrix[2][1], matrix[2][2])