# Продолжите программу, в которой нужно объявить функцию с именем parser_data 
# и следующими параметрами (порядок следования важен):

# text - строка с данными; только позиционные аргументы;
# max_count=0 - максимальное количество выделяемых данных (чисел) из строки; позиционные 
# или именованные аргументы;
# ignore_sign=False - флаг игнорирования знака у числа; только именованные аргументы.
# Функция parser_data должна выделять по порядку из строки text целые числа и возвращать 
# их строковые представления в виде списка. Если целых чисел в text нет, то возвращается 
# пустой список. Количество выделяемых целых чисел не ограничено, если параметр max_count 
# равен нулю. Если же он принимает положительное значение, то выделяются только первые 
# max_count числа. При установке флага (параметра) ignore_sign=True, все знаки перед 
# числами (плюс или минус) должны отбрасываться, иначе они остаются.

# Например:

# res1 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01")
# res2 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01", max_count=7, ignore_sign=False)

# # res1: ['-10', '+40', '4', '-53', '1', '2', '-3', '-0', '01']
# # res2: ['-10', '+40', '4', '-53', '1', '2', '-3']

                  
# Вызовите функцию parser_data для обработки строки:

# data_text = input()

                  
# и со значениями параметров:

# max_count=5
# ignore_sign=True
# Результат сохраните в переменной result.

# здесь объявляйте функцию
def parser_data(text, /, max_count=0, *, ignore_sign=False):
    lst = []
    num = ''
    sign = ''

    if max_count == 0:
        max_count = len(text)

    for i, x in enumerate(text):
        if len(lst) == max_count:
            break
        
        if ignore_sign == False:
            if x == '+' and len(num) == 0:
                sign = '+'
            elif x == '-' and len(num) == 0:
                sign = '-'
        
        if x.isdigit():
            num += x
            if i == len(text)-1:
                lst.append(sign + num)
        elif len(num) != 0:
            lst.append(sign + num)
            num = ''
            if x == '+' and ignore_sign == False:
                sign = '+'
            elif x == '-' and ignore_sign == False:
                sign = '-'
            else:
                sign = ''


    return lst


data_text = 'gdfgd 34 5353 -21-43-11+56 10 abc 20, -5' # input()

# здесь продолжайте программу
result = parser_data(data_text, max_count=5, ignore_sign=True)

print(result)

# res1 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01")
# print(res1) # res1: ['-10', '+40', '4', '-53', '1', '2', '-3', '-0', '01']
# res2 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01", max_count=7, ignore_sign=False)
# print(res2) # res2: ['-10', '+40', '4', '-53', '1', '2', '-3']