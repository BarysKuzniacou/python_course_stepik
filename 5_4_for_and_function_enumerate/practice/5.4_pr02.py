phone_number = input()

lst_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

is_phone_number = True

for i in phone_number:
    if phone_number[0] != '+':
        is_phone_number = False

    if phone_number[1] != '7':
        is_phone_number = False
    if phone_number[2] != '(' or phone_number[6] != ')':
        is_phone_number = False
    if phone_number[10] != '-' or phone_number[13] != '-':
        is_phone_number = False

    if (phone_number[3] not in lst_nums or phone_number[4] not in lst_nums or phone_number[5] not in lst_nums or
             phone_number[7] not in lst_nums or phone_number[8] not in lst_nums or phone_number[9] not in lst_nums or
             phone_number[11] not in lst_nums or phone_number[12] not in lst_nums or
             phone_number[14] not in lst_nums or phone_number[15] not in lst_nums):
         is_phone_number = False

if is_phone_number:
    print('ДА')
else:
    print('НЕТ')