# На вход программе поступают две строки. В каждой строке записаны слова через пробел. 
# Прочитайте эти строки и сохраните их в двух переменных.

# Объявите функцию с двумя параметрами, которой передаются строки со словами и 
# преобразовываются в два списка из слов. Функция должна возвращать кортеж с 
# этими списками в порядке: сначала первый список (первой строки), затем - второй.

# Определите декоратор для этой функции, который из двух списков формирует словарь, 
# в котором ключами являются слова из первого списка, а значениями - соответствующие 
# элементы из второго списка. Длины списков полагаются равными. Полученный словарь 
# должен возвращаться при вызове декоратора.

# Примените декоратор к первой функции и вызовите ее для прочитанных строк. 
# Результат (словарь d) отобразите на экране командой:

# print(*sorted(d.items()))


def form_dict_from_tuple(strs_to_lists):
    def wrapper(*args, **kwargs):  
        res = strs_to_lists(*args, **kwargs)
        dict_res = {}
        for i in range(len(res[0])):
            dict_res[res[0][i]] = res[1][i]
        return dict_res

    return wrapper 

@form_dict_from_tuple
def strs_to_lists(str_1, str_2):
    lst_1 = list(map(str, str_1.split()))
    lst_2 = list(map(str, str_2.split()))
    tuple_lsts = (lst_1, lst_2)
    
    return tuple_lsts


str_in_1 = input()
str_in_2 = input()
# str_in_1 = 'house river tree car'
# str_in_2 = 'дом река дерево машина'

# strs_to_lists = form_dict_from_tuple(strs_to_lists)

d = strs_to_lists(str_in_1, str_in_2)

print(*sorted(d.items()))
