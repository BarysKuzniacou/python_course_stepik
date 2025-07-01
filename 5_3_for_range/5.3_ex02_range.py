# range (start, stop, step)
# range (start, stop)
# range (start)

lst = [1, 2, 3, 4, 5]

print(range(5))
print(list(range(5)))
print(list(range(0)))
print(list(range(0, -5)))
print(list(range(-10, -5)))
print(list(range(-10, -5, 2)))
print(list(range(-10, -5, -2)))
print(list(range(-5, -10, -2)))



for i in range(len(lst)):
    print(lst[i])
