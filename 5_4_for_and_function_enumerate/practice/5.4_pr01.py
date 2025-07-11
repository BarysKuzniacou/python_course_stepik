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

words = 'Барабанщик бил бой в барабан'

lst = []

indx = 0

for i in range(len(words)):
    indx = words.find('ра', i)
    if indx >= 0:
        lst.append(indx)
    elif indx < 0:
        break
    i  += indx + 1

print(lst)


