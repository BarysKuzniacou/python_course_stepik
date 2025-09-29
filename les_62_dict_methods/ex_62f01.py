lst = ['+7', '+6', '+5', '+4']
d = dict.fromkeys(lst) # ключи словаря
print(d) # {'+7': None, '+6': None, '+5': None, '+4': None}
d = dict.fromkeys(lst, 'код страны')
print(d) # {'+7': 'код страны', '+6': 'код страны', '+5': 'код страны', '+4': 'код страны'}

# очистка словаря
d.clear() # очистка словаря
print(d) # {}

# копия
d = {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
d_no_copy = d
d[True] = 0
print(d_no_copy) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
d[True] = 1
d_copy = d.copy()
d[True] = 0
print(d) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
print(d_copy) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}

d_copy_2 = dict(d)
print(id(d), d)
print(id(d_copy_2), d_copy_2)

# получение значения
print(d.get("list")) # [1, 2, 3]
print(d["list"]) # [1, 2, 3], d['list99'] - ошибка
print(d.get("list99")) # None
print(d.get("list99", False)) # False

# возвращает значение по заданному ключу, но если значения нет, то создает ключ
print(d.setdefault('list')) # [1, 2, 3]
print(d.setdefault('list99')) # None
print(d) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5, 'list99': None}
print(d.setdefault('list99')) # None
print(d) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5, 'list99': None}

del d['list99']
d[True] = 1

print(d.setdefault('list99', 99))
print(d) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5, 'list99': 99}

# удаление
d.pop('list99')
print(d) # {True: 0, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
print(d.pop('asd', False))

# удаление последнего значения в словаре
print(d.popitem()) # (5, 5)
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3]}
print(d.popitem()) # ('list', [1, 2, 3])
print(d) # {True: 1, False: 'Ложь'}

# ключи
print(d.keys()) # dict_keys([True, False])
d.clear()
d = {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
print(d.keys()) # dict_keys([True, False, 'list', 5])

for x in d:
    print(x)
# True
# False
# list
# 5

# значения ключей
print(d.values()) # dict_values([1, 'Ложь', [1, 2, 3], 5])

for x in d.values():
    print(x)
# 1
# Ложь
# [1, 2, 3]
# 5

# вывод кортежей ключ - значение
print(d.items()) # dict_items([(True, 1), (False, 'Ложь'), ('list', [1, 2, 3]), (5, 5)])

for x in d.items():
    print(x)
# (True, 1)
# (False, 'Ложь')
# ('list', [1, 2, 3])
# (5, 5)

x, y = (12, '333')
print(x, y) # 12 333

for key, value in d.items():
    print(key, value)
# True 1
# False Ложь
# list [1, 2, 3]
# 5 5

# обновление одного словаря вторым словарем
d_1 = dict(one = 1, two = 2, three = '3', four = '4')
d_2 = {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 'хорошо', 5: 'отлично'}
d_1.update(d_2)
print(d_1) # {'one': 1, 'two': 2, 'three': '3', 'four': 'хорошо', 2: 'неудовлетворительно', 3: 'удовлетворительно', 5: 'отлично'}

# объединение двух словарей 1
d_3 = dict(one = 1, two = 2, three = '3', four = '4')
d_4 = {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 'хорошо', 5: 'отлично'}
d_5 = {**d_3, **d_4}
print(d_5) # {'one': 1, 'two': 2, 'three': '3', 'four': 'хорошо', 2: 'неудовлетворительно', 3: 'удовлетворительно', 5: 'отлично'}
d_6 =  {**d_4, **d_3}
print(d_6) # {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': '4', 5: 'отлично', 'one': 1, 'two': 2, 'three': '3'}
# объединение двух словарей 2
d_7 = d_3 | d_4
print(d_7) # {'one': 1, 'two': 2, 'three': '3', 'four': 'хорошо', 2: 'неудовлетворительно', 3: 'удовлетворительно', 5: 'отлично'}

# keys(): — возвращает коллекцию ключей словаря.
# clear(): — очищает словарь, удаляя все его элементы.
# copy(): — создает копию словаря.
# items(): — возвращает записи в виде кортежей (ключ, значение).
# pop(): — удаляет элемент словаря по ключу и возвращает удаленное значение.
# fromkeys(): — формирует новый словарь с ключами, указанными в списке, и заданным значением по умолчанию.
# values(): — возвращает коллекцию значений словаря.
# get(key, default=None): — возвращает значение по ключу, а если ключ отсутствует, то возвращает default (по умолчанию None).