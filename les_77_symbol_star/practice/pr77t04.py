# Продолжите программу, в которой нужно объявить функцию с именем filter_by_length. Эта функция должна 
# принимать произвольное количество позиционных аргументов, в которые передаются строки, и иметь еще два именованных параметра:

# min_length=0 - минимальная длина строки (целое число, начальное значение 0); принимает только именованные аргументы;
# max_length - максимальная длина строки (без начального значения); принимает только именованные аргументы.
# Функция filter_by_length должна формировать список из переданных строк (позиционные аргументы), но только тех, длины 
# которых лежат в диапазоне [min_length; max_length] включая граничные значения. Сформированный список должен возвращаться этой функцией.

# Например, следующий вызов функции:

# result = filter_by_length("Мономах", "Невский", "Радонежский", "Ломоносов", "Лобачевский", min_length=5, max_length=10)

                  
# должен возвращать список:

# ['Мономах', 'Невский', 'Ломоносов']

# Вызовите функцию filter_by_length для списка имен names_initial и значениями параметров min_length=5, max_length=9. Результат сохраните 
# в переменной names_result.

# P.S. На экран ничего выводить не нужно.

def filter_by_length(*args, min_length=0, max_length):

    res = []

    if len(args) == 1 and isinstance(args[0], list):
        ar = args[0]
    else:
        ar = args

    for s in ar:
        if min_length <= len(s) <= max_length:
            res.append(s)
    
    return res


names_initial = input().split()
names_result = filter_by_length(names_initial, min_length=5, max_length=9)
print(names_result)

# result = filter_by_length("Мономах", "Невский", "Радонежский", "Ломоносов", "Лобачевский", min_length=5, max_length=10)
# print(result)