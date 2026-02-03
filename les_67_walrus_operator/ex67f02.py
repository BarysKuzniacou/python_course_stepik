# примеры реализации

s = 0

d = int(input())
while(d != -1):
    s += d
    d = int(input())

print(s)

s = 0
while (d := int(input())) != -1:
    s += d

print(s)