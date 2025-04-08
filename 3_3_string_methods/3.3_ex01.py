s = 'PyThoN'

print('upper lower')
print(s.upper())
print(s.lower())

print('find')
print(s.find('t'))
print(s.find('T'))
print(s.find('T',3))
print(s.find('T',2))
print(s.find('o',2, 4))

s01 = 'abracadabra'

print('count')
print(s01.count('ra'))
print(s01.count('ra', 4))
print(s01.count('ra', 4, 10))
print(s01.count('ra', 4, 11))

print('find rfind')
print('a', s01.find('a'))
print('a', s01.rfind('a'))

print('index')
print(s01.index('a'))
#print(s01.index('aa')) - выдает ошибку, если не находит

print('replace')
print(s01.replace('a', 'o'))
print(s01.replace('a', 'o', 2))

print('isalpha isdigit')
print('abcdEfG'.isalpha())
print('ab cdEfG'.isalpha())
print('6677'.isdigit())
print('66.77'.isdigit())

print('rjust ljust')
print('abc')
print('abc'.rjust(6))
print('abc'.rjust(6, '8'))
print('abc'.ljust(6))
print('abc'.ljust(6, '8'))

print('split')
print('one two three'.split())
s02 = '1, 2,  3,4'
print(s02.replace(' ', '').split(','))

print('join')
s03 = s02.replace(' ', '').split(',')
print(', '.join(s03))
print(', '.join('Иванов Иван Иванович'.split()))

print('strip rstrip lstrip')
print('               123 123               \n'.strip())
print('               123 123               \n'.rstrip())
print('               123 123               \n'.lstrip())