# список
a = [x ** 2 for x in range(1, 5)]
print(a) # [1, 4, 9, 16]

# множество
a = {x ** 2 for x in range(1, 5)}
print(a) # {16, 1, 4, 9}

# словарь
a = {x: x ** 2 for x in range(1, 5)}
print(a) # {1: 1, 2: 4, 3: 9, 4: 16}

# вариант 1.1
d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d}
print(a) # {1, 2, 3, 4, -4}
# вариант 1.2
set_d = set()
for x in d:
    set_d.add(int(x))

print(set_d) # {1, 2, 3, 4, -4}

# вариант 2.1
m = {'неуд': 2, 'уд': 3, 'хор': '4', 'отл': '5'}
a = {key.upper(): int(value) for key, value in m.items()}
print(a) # {'НЕУД': 2, 'УД': 3, 'ХОР': 4, 'ОТЛ': 5}

# вариант 3.1
d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d if int(x) > 0}
print(a) # {1, 2, 3, 4}

# поменять местами ключи и значения и выбрать значения от 2
m = {'безн': 0, 'убог': 1, 'неуд': 2, 'уд': 3, 'хор': '4', 'отл': '5'}
a = {int(value): key.upper() for key, value in m.items() if int(value) >= 2}
print(a) # {2: 'НЕУД', 3: 'УД', 4: 'ХОР', 5: 'ОТЛ'}