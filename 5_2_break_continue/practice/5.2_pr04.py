# На вход программе подается строка с именами студентов, записанных в одну строчку через пробел.
# Прочитайте эту строку и сформируйте на ее основе список из имен студентов. Необходимо определить, что в этом списке
# хотя бы одно имя начинается и заканчивается на ту же самую букву (без учета регистра). Если это так, то на экран
# вывести строку "ДА", иначе строку "НЕТ". Программу реализовать с использованием цикла while и оператора break.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.2.5
#
# Sample Input:
# Петр Анна Иван Сергей Михаил Федор
# Sample Output:
# ДА

students = list(map(str, input().lower().split()))

number_of_students = len(students)

i = 0

while i < number_of_students:
    word = students[i]
    if word[0] == word[-1]:
        print("ДА")
        break
    i += 1
else:
    print("НЕТ")

