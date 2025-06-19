lst = [3, 7, 9, 11, -5, -4, 33, 28]

flag_find = False

i = 0

while i < len(lst):
    print(i)
    if (lst[i] % 2 == 0):
        print('value' + str(lst[i]))
        break
    else:
        i += 1

i = 0

while i < len(lst):
    print(i)
    flag_find = lst[i] % 2 == 0
    if (flag_find == True):
        break
    else:
        i += 1

print('flag' + str(flag_find))