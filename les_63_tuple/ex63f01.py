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
# 12-21 https://stepik.org/lesson/567048/step/1?auth=login&unit=561322