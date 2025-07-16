a = input().replace('+', ' + ').replace('-', ' - ').split()
s = int(a[0])
for x, i in enumerate(a):
    if i == '+':
        s += int(a[x + 1])
    elif i == '-':
        s -= int(a[x + 1])

print(s)