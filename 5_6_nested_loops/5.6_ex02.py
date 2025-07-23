a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for row in a:
    #print(row, type(row))
    for x in row:
        print(x, type(x), end = ' ')
    print()
