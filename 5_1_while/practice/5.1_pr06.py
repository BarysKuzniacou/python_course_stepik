# На вход программе подается натуральное число (то есть, целое положительное) от трехзначного и более.
# Необходимо прочитать это число и найти произведение всех его цифр. Результат (произведение) вывести на экран.
# Программу реализовать при помощи цикла while.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.1.7
#
# Sample Input:
# 821
# Sample Output:
# 16

number = input()

mult = 1

i = 0

while i < len(number):
    mult *= int(number[i])
    i += 1

print(mult)
