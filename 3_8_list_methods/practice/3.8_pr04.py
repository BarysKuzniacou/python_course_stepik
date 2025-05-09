# На вход программы подается строка с именем, отчеством и фамилией, записанными через пробел. Необходимо прочитать эту строку и представить прочитанные данные в виде новой строки в формате:
#
# Фамилия И.О.
#
# Например, строка: "Сергей Михайлович Балакирев" преобразуется в строку: "Балакирев С.М."
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.8.5
#
# Sample Input:
# Сергей Михайлович Балакирев
# Sample Output:
# Балакирев С.М.

firstName, middleName, lastName = map(str, input().split())
print(f'{lastName} {firstName[0:1]}.{middleName[0:1]}.')
