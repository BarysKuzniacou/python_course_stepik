# Продолжите программу, в которой нужно объявить функцию с именем 
# merge_dicts и следующими параметрами (порядок следования важен):

# dict1 - словарь с данными; принимает позиционные и именованные аргументы;

# ignored_keys=None - набор ключей, которые следует игнорировать в словарях; 
# принимает только именованные аргументы.

# Функция merge_dicts должна выполнять объединение произвольного числа переданных ей словарей в первых позиционных аргументах. 
# При объединении следует пропускать (игнорировать) ключи, из коллекции ignored_keys, если они там определены. 
# Если ignored_keys=None, то никакие ключи не игнорируются. Если при объединении встречаются одинаковые ключи, 
# то их значения следует перезаписывать.

# Функция должна возвращать полученный объединенный словарь. Переданные ей словари меняться не должны.

# Например, при объединении словарей:

# d1 = {"id": 1, "title": "Белая ночь", "author": "Михаил Боярский"}
# d2 = {"id": 2, "name": "Группа крови", "author": "Виктор Цой"}
# d3 = {"id": 3, "track": "На заре", "author": "Альянс"}

# songs = merge_dicts(d1, d2, d3, ignored_keys=('id',))

                  
# должны получить словарь:

# {'title': 'Белая ночь', 'author': 'Альянс', 'name': 'Группа крови', 'track': 'На заре'}

# Вызовите функцию merge_dicts для объединения объявленных в программе словарей goods1, goods2, goods3, goods4 (они не 
# видны в программе, но существуют) с игнорированием полей 'id', 'date' и 'cat_id'. Результат сохраните в переменной goods.

# Задачу следует реализовать, используя только текущие знания, без применения каких-либо внешних библиотек.

# P.S. На экран ничего выводить не нужно.

def merge_dicts(dict1, *args, ignored_keys=None):

    dict_res = {}

    for d in (dict1, *args):
        for key, value in d.items():
            if key and ignored_keys in ignored_keys:
                continue
            else:
                dict_res[key] = value

    # dict_args = {}

    # for d in args:
    #     dict_args |= d

    # dict_res = {**dict1, **dict_args}

    # dict_res_copy = dict_res.copy()

    # if ignored_keys != None:
    #     for key, value in dict_res_copy.items():
    #         for x in ignored_keys:
    #             if key == x:
    #                 dict_res.pop(x, '')

    return dict_res


d1 = {"id": 1, "title": "Белая ночь", "author": "Михаил Боярский"}
d2 = {"id": 2, "name": "Группа крови", "author": "Виктор Цой"}
d3 = {"id": 3, "track": "На заре", "author": "Альянс"}

songs = merge_dicts(d1, d2, d3, ignored_keys=('id',))

print(songs)

# goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id','date', 'cat_id'))

# def merge_dicts(dict1, *args, ignored_keys=None):
#     d = {}
#     for dict_x in (dict1, *args):
#         for key, value in dict_x.items():
#             if ignored_keys and key in ignored_keys:
#                 continue

#             d[key] = value

#     return d


# goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id', 'date', 'cat_id'))