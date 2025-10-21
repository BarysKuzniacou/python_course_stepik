a = 1, 2
print(a) # (1, 2)

a = (1, 2, 3)
print(a) # (1, 2, 3)

a = (1)
print(a) # 1

a = (1,)
print(a) # (1,)

a = 1,
print(a) # (1,)

x, y = (1, 2)
print(x, y) # 1 2

x, y = ['hello', 'python']
print(x, y) # hello python

x, y ='ra'
print(x, y) # r a

a = (1, 2, 3)
print(len(a)) # 3

print(a[0]) # 1
print(a[1]) # 2
print(a[2]) # 3

print(a[1:2]) # (2,)
print(a[0:2]) # (1, 2)
print(a[:2]) # (1, 2)

b = a[:]
print(id(a), id(b)) # 1842425993376 1842425993376

d = {}
d[a] = 'кортеж'
print(d) # {(1, 2, 3): 'кортеж'}

lst = [1, 2, 3]
a = (1, 2, 3)
print(lst.__sizeof__(), a.__sizeof__()) # 72 56

a = () # пустой кортеж
print(a) # ()

# объединение кортежей
a = tuple()
print(a) # ()
print(id(a)) # 140714648719064
a = a + (1,)
print(a) # (1,)
print(id(a)) # 2346375464256
a = a + (6, 7)
print(a) # (1, 6, 7)
a += (('a', 'hello'),)
print(a) # (1, 6, 7, ('a', 'hello'))

a = (0,) * 10
print(a) # (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
a = ('hello', 'world')
a = a * 5
print(a)

a = tuple([1, 2, 3])
print(a) # (1, 2, 3)

a = tuple('hello')
print(a) # ('h', 'e', 'l', 'l', 'o')

# преобразование кортежа в список
t = (1, 2, 3)
print(t) # (1, 2, 3)
lst = list(t)
print(lst) # [1, 2, 3]

# ссылку менять нельзя, но значения по ссылке менять можно, если она не приведет к 
# созданию нового объекта
a = (True, [1, 2, 3], 'hello', 5, {'house': 'дом'})
print(a) # (True, [1, 2, 3], 'hello', 5, {'house': 'дом'})
print(a[1]) # [1, 2, 3]
a[1].append('5')
print(a) # (True, [1, 2, 3, '5'], 'hello', 5, {'house': 'дом'})

# toupe.count(значение) - возвращает число найденных элементов с указанным значением
a = ('abc', 2, [1, 2], True, 2, 5)
print(a.count('abc')) # 1
print(a.count(2)) # 2
print(a.count('hello')) # 0

# touple.index(значение[, start[,stop]]) - возвращает индекс первого найденного 
# элемента с указанным значением (start и stop - необязательные параметры, индексы 
# начала и конца поиска)
print(a.index('abc')) # 0
print(a.index(2)) # 1
print(a.index(2, 2)) # 4
# print(a.index(2, 2, 3)) # ошибка
# print(a.index('hello')) # ошибка

# in - поиск значения в кортеже
print(3 in a) # False
print([1, 2] in a) # True