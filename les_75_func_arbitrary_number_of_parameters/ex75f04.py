def os_path(*args, **kwargs):
    print(kwargs) # словарь
    path = kwargs['sep'].join(args)
    return path


print(os_path('F:\\~stepik.org', 
              'Добрый, добрый Python (Питон)', 
              '39\\p39. Функции.docx',
              sep='/', trim=True))