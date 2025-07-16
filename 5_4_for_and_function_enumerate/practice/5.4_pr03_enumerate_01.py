exp = input().replace(' ', '')
summ = 0

for val in exp.split('+'):
    for i, v in enumerate(val.split('-')):
        if i == 0:
            summ += int(v)
        else:
            summ -= int(v)

print(summ)