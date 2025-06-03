x = int(input())

if x < 0:
    print('error')
elif 0 <= x <= 9:
    print('x - 0')
elif  10 <= x <= 99:
    print('x - 00')
elif  100 <= x <= 999:
    print('x - 000')
else:
    print('x - 0000')