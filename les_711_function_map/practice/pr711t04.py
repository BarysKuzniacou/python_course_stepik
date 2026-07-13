# На вход программы подается строка с целыми числами, записанными через пробел. Необходимо 
# ее прочитать и с помощью функций map() и list() преобразовать в список digits, состоящий 
# из целых чисел (в порядке их следования в строке). Затем, используя список digits, нужно 
# сформировать еще один список result, который бы состоял из булевых значений True/False:

# True - если текущее число в списке digits кратно 7 (делится нацело на 7);
# False - в противном случае.
# Список digits должен оставаться неизменным. Выведите на экран полученный список result командой:

# print(*result)

# test #1
# input: 5 3 10 17 21 78 -54 -20
# output: False False False False True False False False

# test #2
# input: -7 21 14 77 -35
# output: True True True True True

# test #3
# input: 55 20 1 5 81 4
# output: False False False False False False

# s_input = input()

s_input = '55 20 1 5 81 4'

digits = list(map(int, s_input.split()))
# result = [x % 7 == 0 for x in digits]
result = list(map(lambda n: n % 7 == 0, digits))

print(*result)
