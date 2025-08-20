a = float(input('a: '))
b = float(input('b: '))

if a < b:
    a, b = b, a

print(f'a: {a}, b: {b}')