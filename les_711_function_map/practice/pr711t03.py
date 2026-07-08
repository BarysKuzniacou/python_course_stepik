# На вход программы подается строка, которую необходимо прочитать. Затем, используя 
# функцию map(), заменить в этой строке символы латинского 
# алфавита 'b', 'i', 't', 'B', 'I', 'T' на символ '#', а остальные 
# символы оставить неизменными. Вывести на экран преобразованную строку.

# Например, для входной строки:

# "Python is the best language!"
 
# должен формироваться следующий вывод на экран:

# Py#hon #s #he #es# language!

# s = input()

s = 'Строка без замены символов'

change_char = ['b', 'i', 't', 'B', 'I', 'T']

s_changed = map(lambda c: '#' if c in change_char else c, s)

res = ''

for x in s_changed:
    res += x

print(res)

# st = input()
# new_st = ''.join(list(map(lambda s: '#' if s in 'bitBIT' else s, st)))
# print(new_st)

# s = input()
# stroka_lst = list(map(lambda x: x if x not in {"b", "i", "t", "B", "I", "T"} else '#', s))
# stroka = "".join(stroka_lst)
# print(stroka)