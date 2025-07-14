# На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра".
# Выведите найденные индексы на экран в одну строчку через пробел. Если же фрагмент "ра" отсутствует в строке,
# то вывести -1.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.1
#
# Sample Input:
# Барабанщик бил бой в барабан
# Sample Output:
# 2 23
from os import lstat

from pyexpat.errors import messages


#words = 'Барабанщик бил бой в барабан'
# output: 2 23
#words = 'Евгений Онегин'
# output: -1
#words = 'Одинокий рабочий долго работал на работе'
# output: 9 23 34
#words = 'рар'
# output: 0
#words = 'Одинокий рабочий долго работал на рботе'
# output: 9 23
#words = 'Арарат'
# output: 1 3

def count_pa(words):
    lst = []

    for i in range(len(words) - 1):
        if words.find('ра') == -1:
            lst.append(-1)
            break
        if words[i] == 'р' and words[i + 1] == 'а':
            lst.append(i)
            i += 1

    return lst

data_lst = ['Барабанщик бил бой в барабан', 'Евгений Онегин', 'Одинокий рабочий долго работал на работе',
            'рар', 'Одинокий рабочий долго работал на рботе', 'Арарат']
#message = f'данные {words} : {lst}'

for data in data_lst:
    lst_res = count_pa(data)
    #print(message.format(words = data, lst = lst_res))
    print(*lst_res)

# words = input()
#
# lst = []
#
# indx = 0
#
# for i in range (len(words)-1):
#     if words.find('ра') == -1:
#         lst.append(-1)
#         break
#     if words[i] == 'р' and words[i+1] == 'а':
#         lst.append(i)
#         i += 1
#
# print(*lst)

# string = input().lower()
#
# if 'ра' in string:
#     for index, value in enumerate(string):
#         if string[index:index+2] == 'ра':
#             print(index, end=' ')
# else:
#     print(-1)