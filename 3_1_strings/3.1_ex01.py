s1 = "Панда"
s2 = 'Panda'
print(s1, s2)

text = '''Первая строка
Втроая строка
Третья строка'''
print(text)

empty = ''
print(empty)

space = ' '
print(space)

s3 = 'first'
s4 = 'second'
print(s3 + s4)
print(s3 + " " + s4)

# строки можно соединять только со строками. ошибка - print(s3 + 5)
print(s3 + str(5))

s5 = True
print(str(s5) + str(7), type(s5)) # s5 перед выводом будет преобразована в строку, но тип не поменяет

# duplicate string
s6 = 'tra'
s7 = '-ta'
print(s6 + (s7 * 3)) # tra-ta-ta-ta

# len() - вычисляет длину строки
s8 = '12345678'
print(len(s8))

# in проверяет вхождение подстроки в строке
s9 = 'ab'
s10 = 'abracadabra'
print(s9 in s10) # вернет булевое True
s11 = "AB"
print(s11 in s10) # вернет False

# сравнение строк
s12 = 'Hello'
s13 = 'hello'
print(s12 == s13) # вернет False
s14 = ' hello '
print(s14 == s13) # вернет False, т.к. считает и пробелы за символ

s15 = '123'
s16 = '456'
print(s15 > s16) # лексикографическое сравнение строк
print(s15 == s16)
print(s15 < s16)
print('"кит" < "кот":', "кит" < "кот") # о < и
print('"кит" < "коя":', "кит" < "коя") # о < и, а последующие символы игнорируются
print('"ABC" < "Abc":', "ABC" < "Abc") #  True, т.к. заглавные символы идут до малых по ASCII

# ord() - код ASCII
print(ord('A'))
print(ord('a'))