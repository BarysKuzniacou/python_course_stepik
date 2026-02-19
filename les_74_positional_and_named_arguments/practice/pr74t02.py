# Объявите в программе функцию с именем check_password, которая первым параметром принимает строку (пароль) 
# и имеет второй параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять, 
# есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов. Если проверка 
# проходит, то функция возвращает булево True, иначе False.

# P. S. Вызывать функцию не нужно, только объявить.

# Sample Input:

# 12345678!
# Sample Output:

# True

# test #1
# input: 12345678!
# output: True

# test #2
# input: 4364#
# output: False

# test #3
# input: dfghfgh8gf7h6f
# output: False

# test #4
# input: 5657dfgfh098A!@#
# output: True

def check_password(password, chars='$%!?@#'):

    check_sym = False
    check_len = False

    for i in chars:
        if i in password:
            check_sym = True
            break
    
    if len(password) > 7:
        check_len = True
    
    return check_len and check_sym


print(check_password('12345678!'))
print(check_password('4364#'))
print(check_password('dfghfgh8gf7h6f'))
print(check_password('5657dfgfh098A!@#'))

# def check_password(str, chars="$%!?@#"):    
#     return len(set(str) & set(chars)) != 0 and len(str) > 7

# def check_password(st, chars='$%!?@#'):
#     return len(st) >= 8 and any(i in chars for i in st)