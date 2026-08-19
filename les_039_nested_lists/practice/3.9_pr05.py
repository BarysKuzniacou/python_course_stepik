# Объявите в программе вложенный список (двумерный) с именем table, содержащий следующие значения:
# table = [[6, -2, 0, -5.4, 'abc'], [True, 'pt', 3, False, True], [1, 1, 1, 0]]

# Здесь каждая строка таблицы должна описываться своим отдельным вложенным списком. Формат списка table следующий:

# table = [[значение1, значение2, ... значениеN], [значение1, значение2, ... значениеM], ...]
  
# Необходимо со списком table выполнить следующие действия:

# добавить в конец списка table еще одну строку (вложенный список) со значениями: 4, -2, 10, 6, 2, 7, 13;
# поменять местами первую и последнюю добавленную строку.

table = [[6, -2, 0, -5.4, "abc"], [True, "pt", 3, False, False, True], [1, 1, 1, 0]]

lst = [4, -2, 10, 6, 2, 7, 13]

table.append(lst)

# 1
# table_new = []

# for i in range(len(table)):
#     if i == 0:
#         table_new.append(table[len(table)-1])
#     elif i == (len(table) - 1):
#         table_new.append(table[0])
#     else:
#         table_new.append(table[i])

# table = table_new

# 2
# table = [table[len(table)-1], table[1], table[2], table[0]]

# print(table_new)

# 3
table[0], table[len(table)-1] = table[len(table)-1], table[0]

# print(table)