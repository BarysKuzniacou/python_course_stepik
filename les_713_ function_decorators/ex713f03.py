def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('что-то делаем перед вызовом функции func')
        func(*args, **kwargs)
        print('что-то делаем после вызова функции func')
    
    return wrapper


def some_func(title):
    print(f'title = {title}')


some_func = func_decorator(some_func)
some_func('python')