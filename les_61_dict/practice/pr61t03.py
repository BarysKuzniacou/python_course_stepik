# На вход программе подаются данные в формате ключ=значение, записанные через пробел. Необходимо прочитать строку с
# этими данными и на их основе сформировать словарь. Затем проверить, существуют ли в словаре ключи: 'house', 'True'
# и '5' (все ключи - строки). Если все они существуют, то вывести на экран "ДА", иначе "НЕТ".
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.1.5
#
# Sample Input:
# вологда=город house=дом True=1 5=отлично 9=божественно
# Sample Output:
# ДА

# test #1
# input: вологда=город house=дом True=1 5=отлично 9=божественно
# output: ДА
#
# test #2
# input: самара=город дом=house 1=True отлично=5 превосходно=8
# output: НЕТ
#
# test #3
# input: москва=город house=дом True=1 5=отлично road=дорога False=0
# output: ДА
#
# test #4
# input: москва=город house=дом 5=отлично road=дорога False=0
# output: НЕТ
#
# test #5
# input: москва=город True=1 5=отлично road=дорога False=0
# output: НЕТ
#
# test #6
# input: москва=город 5=отлично road=дорога False=0
# output: НЕТ
#
# test #7
# input: москва=город house=дом True=1 road=дорога False=0
# output: НЕТ
#
# test #8
# input: house=дом
# output: НЕТ

#s = 'вологда=город house=дом True=1 5=отлично 9=божественно'
#s = s.replace('=', ' ')
#lst = list(s.split())

lst = list(input().replace('=', ' ').split())

lst_for_dict = [[lst[i], lst[i+1]] for i in range(0, len(lst), 2)]

d = dict(lst_for_dict)

print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

# d = dict([x.split('=') for x in input().split()])