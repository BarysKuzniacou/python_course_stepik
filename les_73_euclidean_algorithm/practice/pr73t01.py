# Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. 
# В программе необходимо объявить функцию get_nod с двумя параметрами a и b (натуральные числа) и возвращающую значение НОД(a, b).

# P. S. Вызывать функцию не нужно, только задать. Постарайтесь реализовать алгоритм, не возвращаясь к материалу на видео.

# Sample Input:

# 15 121050
# Sample Output:

# 15

def get_nod(a, b):
    if a < b:
        a, b = b, a

    # div = 0

    # r = 1

    # while r != 0:
    #     r = a % b

    #     if r == 0:
    #         div = b
    #     else:
    #         a = b
    #         b = r
        
    # return div

    while b != 0:
        a, b = b, a % b
    
    return a


def test_nod(func):
    # test 1
    a = 15
    b = 121050
    
    res = func(a, b)

    if res == 15:
        print('test 1 - ok')
    else:
        print('test 1 - fail')
    
    # test 2
    a = 11
    b = 33
    
    res = func(a, b)

    if res == 11:
        print('test 3 - ok')
    else:
        print('test 2 - fail')

    # test 3
    a = 2
    b = 1001
    
    res = func(a, b)

    if res == 1:
        print('test 3 - ok')
    else:
        print('test 3 - fail')


test_nod(get_nod)


