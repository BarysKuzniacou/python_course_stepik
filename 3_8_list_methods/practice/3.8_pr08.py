# На вход программы подается строка с названиями рек, записанными в одну строчку через пробел. Необходимо
# прочитать строку и сформировать список lst из названий рек. Затем, отсортировать по возрастанию полученный
# список по названиям и в отсортированном списке удалить первый элемент. Результирующий список отобразить на
# экране в одну строчку через пробел с помощью команды:
#
# print(*lst)
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.8.10
#
# Sample Input:
# Лена Обь Волга Дон Енисей
# Sample Output:
# Дон Енисей Лена Обь

lst = input().split()
lst.sort()
lst.pop(0)
print(*lst)
