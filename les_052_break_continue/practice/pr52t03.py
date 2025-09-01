# На вход программе подается строка с названиями городов, записанных в одну строчку через пробел.
# Прочитайте эту строку и сформируйте на ее основе список из названий городов. Необходимо определить, что в этом списке
# все города имеют длину более 5 символов. Если это так, то на экран вывести строку "ДА", иначе строку "НЕТ".
# Программу реализовать с использованием цикла while и оператора break.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.2.4
#
# Sample Input:
# Самара Ульяновск Новгород Воронеж
# Sample Output:
# ДА

cities = list(map(str, input().split()))

number_of_cities = len(cities)

i = 0

while i < number_of_cities:
    if len(cities[i]) >= 5:
        i += 1
#        if i == number_of_cities:
#            print("ДА")
    else:
        print("НЕТ")
        break
else:
    print("ДА")