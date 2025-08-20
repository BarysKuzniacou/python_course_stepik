a, b, c = map(int, input().split())

if a > b:
    if a > c:
        print('a - max')
    else:
        print('c - max')
else:
    if b > c:
        print('b - max')
    else:
        print('c - max')
