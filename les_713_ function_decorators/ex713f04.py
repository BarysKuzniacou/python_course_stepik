def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('что-то делаем перед вызовом функции func')
        res = func(*args, **kwargs)
        print('что-то делаем после вызова функции func')
        return res
    
    return wrapper


def some_func(title, tag):
    print(f'title = {title}, tag = {tag}')
    return f'<{tag}>{title}</{tag}>'


some_func = func_decorator(some_func)
res = some_func('python', 'h1')
print(res)
