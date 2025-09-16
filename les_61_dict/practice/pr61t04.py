# На вход программе подаются данные в формате ключ=значение, записанные через пробел. Необходимо прочитать строку с
# этими данными и на их основе сформировать словарь d. Затем удалить из этого словаря ключи 'False' и '3', если они
# существуют. Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:
#
# print(*sorted(d.items()))
#
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.6
#
# Sample Input:
# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
# Sample Output:
# ('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')

d = dict([x.split('=') for x in input().split()])

if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']

print(*sorted(d.items()))

# s = [i.split('=') for i in input().split()]
# d = {i: v for i, v in s}
# if 'False' in d:
#     del d['False']
# if '3' in d:
#     del d['3']
#
# print(*sorted(d.items()))

# d = dict([i.split('=') for i in input().split()])
# del_values = [ 'False', '3']
#
# for i in del_values:
#     if i in d:
#         del d[i]
#
# print(*sorted(d.items()))