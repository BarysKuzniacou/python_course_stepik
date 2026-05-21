N = 100

def my_func_1():
    N = 20
    print(N)


def my_func_2():
    global N
    N = 200
    print(N)


print(N)
my_func_1()
my_func_2()
print(N)