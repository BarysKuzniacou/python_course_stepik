def os_path(*args, sep='\\'):
    path = '\\'.join(args)
    return path


print(os_path('F:\\~stepik.org', 
              'Добрый, добрый Python (Питон)', 
              '39\\p39. Функции.docx',
              sep='/'))