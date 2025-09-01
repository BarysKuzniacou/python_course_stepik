# На вход программе подаются строки (URL-адреса, каждая с новой строки). В программе уже реализовано их чтение
# и сохранение в списке:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Требуется заменить в строках списка lst_in все пробелы на символ дефиса (-). Следует учесть, что может быть
# несколько подряд идущих пробелов. Полученные URL-адреса (строки) вывести на экран в столбик в порядке их
# следования в списке lst_in.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.2
#
# Sample Input:
# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
# Sample Output:
# django-chto-eto-takoe-poryadok-ustanovki
# model-mtv-marshrutizaciya-funkcii-predstavleniya
# marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya

lst_in = ['django chto  eto takoe    poryadok ustanovki',
          'model mtv   marshrutizaciya funkcii  predstavleniya',
          'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']

for i, line in enumerate(lst_in):
    while line.count('  '):
        line = line.replace('  ', ' ')
    lst_in[i] = line

for i, line in enumerate(lst_in):
    while line.count(' '):
        line = line.replace(' ', '-')
    lst_in[i] = line

for i, line in enumerate(lst_in):
    print(lst_in[i])