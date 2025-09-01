A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

A2 = [[x ** 2 for x in row] for row in A]
A1 = [x ** 2 for row in A for x in row]

print(A2)
print(A1)