d = [4, 3, -5, 0, 2, 11, 122, -8, 9]

a = ['четное' if x % 2 == 0 else 'нечетное'
     for x in d
     if x > 0]

print(a)