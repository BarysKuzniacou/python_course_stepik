# На вход программе подаются данные в формате ключ=значение, записанные через пробел. Значениями здесь являются
# целые числа (см. пример ниже). Необходимо прочитать строку с этими данными и на их основе сформировать словарь d,
# используя функцию dict(). Результирующий словарь вывести на экран командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# one=1 two=2 three=3
# Sample Output:
# ('one', 1) ('three', 3) ('two', 2)

#s = 'one=1 two=2 three=3'

lst = list((input().replace("=", ' ')).split())

lst_for_dict = [[lst[i], int(lst[i+1])] for i in range(0, len(lst), 2)]

d = dict(lst_for_dict)

print(*sorted(d.items()))
