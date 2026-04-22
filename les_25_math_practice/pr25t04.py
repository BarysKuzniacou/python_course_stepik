# В программе выполняется чтение натурального четырехзначного числа (например, 3247):

# digit = int(input())

                  
# Необходимо вычислить сумму всех его цифр и результат (сумму) сохранить 
# в переменной sum_digit. Например, для числа 3247 сумма равна:

# S = 3 + 2 + 4 + 7 = 16

# P.S. На экран ничего выводить не нужно.

# digit = int(input())

digit = 3247

# a = int(digit/1000)
# b = int(digit / 100) - (int(digit/1000) * 10)
# c = int(digit / 10) - ((int(digit/1000) * 100) + ((int(digit / 100) - (int(digit/1000) * 10)) * 10))
# d = digit - (int(digit/1000) * 1000) - ((int(digit / 100) - (int(digit/1000) * 10)) * 100) - ((int(digit / 10) - ((int(digit/1000) * 100) + ((int(digit / 100) - (int(digit/1000) * 10)) * 10))) * 10)

# sum_digit = int(digit/1000) + (int(digit / 100) - int(digit/1000) * 10) + (int(digit / 10) - int(digit/1000 * 100) - (int(digit / 100) - int(digit/1000) * 10)) + (digit - (int(digit / 10) - int(digit/1000 * 100) - (int(digit / 100) - int(digit/1000) * 10)))

a = int(digit % 10000 / 1000)
b = int(digit % 1000 / 100)
c = int(digit % 100 / 10)
d = digit % 10

# print(a, b, c, d)

sum_digit = a + b + c + d

print(sum_digit)
