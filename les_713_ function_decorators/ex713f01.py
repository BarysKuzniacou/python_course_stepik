def func_decorator(func):
    def wrapper():
        print('что-то делаем перед вызовом функции func')
        func()
        print('что-то делаем после вызова функции func')
    
    return wrapper


def some_func():
    print('Вызов функции some_func')


some_func()
print('работа декоратора:')
some_func = func_decorator(some_func)
some_func()