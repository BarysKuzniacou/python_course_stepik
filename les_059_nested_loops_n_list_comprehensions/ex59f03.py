matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

a = [x
     for row in matrix
     for x in row]

print(a)