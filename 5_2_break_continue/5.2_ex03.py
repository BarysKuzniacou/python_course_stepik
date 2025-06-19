sum = 0

value = 1

while value != 0:
    value = int(input('enter value: '))
    if value % 2 == 0:
        continue
    sum += value
    print('sum: ', sum)