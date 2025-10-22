# На вход программе подается строка с названиями городов, записанных через пробел. 
# Необходимо прочитать эту строку и на ее основе сформировать кортеж из названий городов. 
# Затем, выполните проверку: если в полученном кортеже присутствует город "Ульяновск", то 
# этот элемент следует удалить (создав новый кортеж). Выведите на экран названия городов 
# из итогового кортежа (по порядку) в одну строчку через пробел.
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.3.5
# Sample Input:
# Воронеж Самара Тольятти Ульяновск Пермь
# Sample Output:
# Воронеж Самара Тольятти Пермь

lst = list(input().split())

t = tuple(lst)

if 'Ульяновск' in t:
    lst.remove('Ульяновск')
    t = tuple(lst)

print(*t)

# t = tuple(input().split())
# t = tuple(v for v in t if v != 'Ульяновск') 
# print(*t)

# cities = tuple(input().split())
# if "Ульяновск" in cities:
#     idx = cities.index("Ульяновск")
#     cities = cities[:idx] + cities[idx+1:]
# print(*cities)

# t = tuple(input().split())
# if 'Ульяновск' in t:
#     tmp = list(t)
#     tmp.remove('Ульяновск')
#     t = tuple(tmp)
# print(*t)