sum = 0
i = 10 # -10

while i < 100:
    print('i ', i)
    if i == 0:
        break
    sum += 1/i
    print('sum ', sum)
    i += 1
else:
    print('correct')

print('final sum ', sum)