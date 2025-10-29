a = {1, 2, 3, 'hello'}
print(a, type(a)) # {1, 2, 3, 'hello'} <class 'set'>

# множества содержат только уникальные значения
a = {1, 2, 3, 'hello', 2, 3, 'hello'}
print(a, type(a)) # {1, 2, 3, 'hello'} <class 'set'>

# элементами множества могут быть только неизменяемые типы данных
# можно: числа, булевые значения, строки, кортежи
# нельзя: списки, словари, другие множества

# пустое множество
a = set()
b = {}
print(f'{a} is {type(a)}, {b} is {type(b)}') # set() is <class 'set'>, {} is <class 'dict'>

# список в множестве
a = set([0, -1, 1, 2, 1, 2]) # {0, 1, 2, -1}
print(a)

print(set('abracadabra')) # {'d', 'r', 'c', 'a', 'b'}
print(set(range(7))) # {0, 1, 2, 3, 4, 5, 6}

cities = ['Boston', 'Everton', 'London', 'Lids','Everton','Boston',]
set_cities = set(cities)
print(set_cities) # {'Boston', 'Lids', 'Everton', 'London'} / {'Boston', 'London', 'Lids', 'Everton'}
cities_list = list(set_cities)
print(cities_list) # ['Boston', 'Lids', 'Everton', 'London'] / ['Boston', 'London', 'Lids', 'Everton']

# перебор значений в ножестве
for city in set_cities:
    print(city, end=' ') # Boston London Lids Everton / London Lids Everton Boston London

print('')

it = iter(set_cities)
print(next(it)) # Everton
print(next(it)) # Boston
print(next(it)) # London
print(next(it)) # Lids

print(len(set_cities)) # 4

# присутствие в множестве элемента
print('York' in set_cities) # False

# добавление элемента во множество
# add
a = set()
a. add(1)
print(a) # {1}
a. add(1)
print(a) # {1}
a. add(2)
print(a) # {1, 2}
# update
a.update([3, 4, 'hello'])
print(a) # {1, 2, 3, 4, 'hello'}
a.update('abracadabra')
print(a) # {1, 2, 3, 4, 'r', 'hello', 'b', 'd', 'a', 'c'}

# удаление значения из множества
# discard
a.discard('hello')
print(a) # {1, 2, 3, 4, 'r', 'b', 'd', 'a', 'c'}
a.discard('hello')
print(a) # {1, 2, 3, 4, 'r', 'b', 'd', 'a', 'c'}
# remove
a.remove('r')
print(a) # {1, 2, 3, 4, 'a', 'd', 'b', 'c'}
# pop - удаление произвольного элемента
print(a.pop()) # 1
print(a) # {2, 3, 4, 'd', 'c', 'a', 'b'}
# clear - удаление всех элементов из множества
a.clear()
print(a) # set()