# На вход программе подается строка, содержащая латинские символы, пробелы и цифры. 
# Необходимо прочитать эту строку и выделить из нее все неповторяющиеся цифры (символы от 0 до 9). 
# Выведите на экран все найденные уникальные цифры в одну строчку через пробел в порядке возрастания 
# их значений. Если цифры отсутствуют, то вывести строку "НЕТ".
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.4.5
# Sample Input:
# Python 3.9.11 - best language!
# Sample Output:
# 1 3 9

str_in = input()

set_out = set()

for c in str_in:
    if c.isdigit() == True:
        set_out.add(int(c))

# for c in str_in:
#     if c == '0':
#         set_out.add(0)
#     elif c == '1':
#         set_out.add(1)
#     elif c == '2':
#         set_out.add(2)
#     elif c == '3':
#         set_out.add(3)
#     elif c == '4':
#         set_out.add(4)
#     elif c == '5':
#         set_out.add(5)
#     elif c == '6':
#         set_out.add(6)
#     elif c == '7':
#         set_out.add(7)
#     elif c == '8':
#         set_out.add(8)
#     elif c == '9':
#         set_out.add(9)
#     elif c == '0':
#         set_out.add(0)

if(len(set_out) == 0):
    print('НЕТ')
else:
    print(*sorted(set_out))

# print(*sorted(set(int(c) for c in input() if c.isdigit())) or ['НЕТ'])

# st = set([x for x in input() if x.isdigit()])
# if st:
#     print(*sorted(st))
# else:
#     print('НЕТ')

# print(*sorted(set(input()) & set('0123456789')) or ['НЕТ'])
       
