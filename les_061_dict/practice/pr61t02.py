# На вход программе поступают данные в виде набора строк в формате:
#
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
#
# Ключами здесь выступают целые числа (см. пример ниже). В программе уже реализовано считывание всех строк и
# сохранение их в виде списка:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Необходимо преобразовать список lst_in в словарь d (без использования функции dict()) и вывести полученный словарь
# на экран командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# 5=отлично
# 4=хорошо
# 3=удовлетворительно
# Sample Output:
# (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')

lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']

lst = []

d ={}

for i in range(len(lst_in)):
    lst.append((str(lst_in[i]).replace("=", ' ')).split())

for i in range(0, len(lst)):
    d[int(lst[i][0])] = lst[i][1]

print(*sorted(d.items()))

# d = {}
# for i in lst_in:
#     key, value = i.split('=')
#     d[int(key)] = value
#
# print(*sorted(d.items()))

# d = {}
# for s in lst_in:
#     row = s.split('=')
#     d[int(row[0])] = row[1]
#
# print(*sorted(d.items()))

# d = {}
# for i in lst_in:
#   d[int(i[0])] = i[2:]
#
# print(*sorted(d.items()))


