# На вход программе подается семизначное целое положительное число. Необходимо его прочитать и с помощью list
# comprehension сформировать список lst, содержащий цифры этого числа (в списке должны быть записаны числа, а не
# строки). Полученный список вывести на экран командой:
#
# print(lst)
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.8.2
#
# Sample Input:
# 4567397
# Sample Output:
# [4, 5, 6, 7, 3, 9, 7]

s_input = input()

lst = [int(x) for x in s_input]

print(lst)