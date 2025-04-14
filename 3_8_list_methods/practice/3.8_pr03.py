# На вход программы подается строка с номером телефона в формате:
#
# +7(xxx)xxx-xx-xx
#
# Необходимо прочитать эту строку и преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. Отобразить полученный список на экране командой:
#
# print("".join(lst))
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.8.4
#
# Sample Input:
#
# +7(912)123-45-67
# Sample Output:
#
# 8(912)1234567

#telephoneNumber = '+7(912)123-45-67'
telephoneNumber = input()
print(telephoneNumber)
telephoneNumber = telephoneNumber.replace("-", "")
lst = list(telephoneNumber.split())
print(lst)

lst.remove('+')
indexOf7 = lst.index('7')
lst[indexOf7] = '8'


print("".join(lst))