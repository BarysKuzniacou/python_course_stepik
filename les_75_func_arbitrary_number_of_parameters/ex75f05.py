def os_path(disk , *args, sep='\\', **kwargs):
    args = (disk, ) + args

    if 'trim' in kwargs and kwargs['trim']==True:
        args = [x.strip() for x in args]

    path = sep.join(args)
    return path


print(os_path('F:\\', '         ~stepik.org', 
              'Добрый, добрый Python (Питон)         ', 
              '39\\p39. Функции.docx',
              trim=False))