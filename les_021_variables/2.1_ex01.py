a = 7
print(a)

b = 9
b = 10.2
print(b)

b = "Hello" # переменные не хранят значения, а ссылаются на объект
print(b)

a = b = c = 0
print(a , b , c)
print(id(a) , id(b), id(c)) # id() выводит идентификатор объекта

a, b, c = 1, 2, 3 # множественное присваивание
print(id(a) , id(b), id(c))
a, b, c = 1, 1, 1
print(id(a) , id(b), id(c))

# изменение значений переменных
a = 0
b = 1
print(a, b)
a, b = b, a
print(a, b)

# type() возвращает тип данных переменной
a = 1
b = 2.2
c = "Hello"
print(type(a), type(b), type(c))
