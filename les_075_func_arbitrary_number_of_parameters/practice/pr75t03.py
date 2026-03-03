# Объявите в программе функцию с именем get_data_fig для вычисления периметра произвольного N-угольника. 
# На вход этой функции передаются N длин сторон через ее аргументы. Дополнительно могут быть указаны именованные аргументы:

# tp - булево значение True/False;
# color - целое числовое значение;
# closed - булево значение True/False;
# width - вещественное значение.
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке их 
# перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).

# P.S. Функцию выполнять не нужно, только объявить.

# Sample Input:

# 1 2 3 4 3 2 4
# Sample Output:

# 19
# 19 True
# 19 True 7
# 19 False 2.0

def get_data_fig(*lens, **kwargs): #tp=True, color=0, closed=True, width=0.0
    p = sum(lens)

    res = list()

    res.append(p)

    if 'tp' in kwargs:
        res.append(kwargs['tp'])
    
    if 'color' in kwargs:
        res.append(kwargs['color'])

    if 'closed' in kwargs:
        res.append(kwargs['closed'])

    if 'width' in kwargs:
        res.append(kwargs['width'])

    return tuple(res)


print(get_data_fig(1, 2, 3, 4, 3, 2, 4, tp=True, color=0, closed=True, width=0.0))

# def get_data_fig(*args, **kwargs):
#     kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs] 
#     return (sum(args), *kwargs)