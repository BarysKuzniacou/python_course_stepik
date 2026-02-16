import time

def get_min_equal_divider(a, b):
    '''
    Вычисляется НОД по алгоритму Евклида.
    :param a: первое натуральное число.
    :param b: второе натуральное число.
    :return: НОД
    '''

    while a != b:
        if a > b:
            a -= b
        else: 
            b -= a
    
    return a


def get_min_equal_divider_new(a, b):

    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    
    
    return a



def test_min_equal_divider(func):
    # test 1
    a = 28
    b = 35
    
    res = func(a, b)

    if res == 7:
        print('test 1 - ok')
    else:
        print('test 1 - fail')

    # test 2
    a = 100
    b = 1
    
    res = func(a, b)

    if res == 1:
        print('test 2 - ok')
    else:
        print('test 2 - fail')

    # test 3
    a = 2
    b = 100000000
    
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st

    if res == 2 and dt < 1:
        print('test 3 - ok')
    else:
        print('test 3 - fail')

# res = get_min_equal_divider(18, 24)
# print(res)
# help(get_min_equal_divider)

#test_min_equal_divider(get_min_equal_divider)

test_min_equal_divider(get_min_equal_divider_new)