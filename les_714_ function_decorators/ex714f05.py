import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'время работы = {dt}')
        return res
    
    return wrapper

@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
 
    return a


# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)
res1 = get_nod(2, 100000)
res2 = get_fast_nod(2, 100000)
print(res1, res2)

