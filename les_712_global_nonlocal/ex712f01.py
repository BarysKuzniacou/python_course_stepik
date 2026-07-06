N = 100

def my_func_1():
    N = 20
    print('func 1', N)


def my_func_2():
    global N
    N = 200
    print('func 2', N)


print(N)
my_func_1()
my_func_2()
print(N)