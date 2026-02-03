if var := 5 + 2:
    print(var)

if d := int(input('введите число: ')):
    print(d)

if d := int(input('введите число (5): ')) > 0: # True
    print(d)

if (d := int(input('введите число (5): '))) > 0: # True
    print(d)