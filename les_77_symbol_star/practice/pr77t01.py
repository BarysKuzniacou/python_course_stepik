# Продолжите программу, в которой нужно объявить функцию с именем most_popular и следующими 
# параметрами (порядок следования важен):

# people - список строк из имен людей; должен принимать позиционные и именованные аргументы;
# case_sens=False - флаг учета регистра букв (малые или большие) при обработке строк (по умолчанию 
# значение False); должен принимать только именованные аргументы.
# Функция most_popular должна находить наиболее часто встречающееся имя в списке people. Если 
# установлен флаг case_sens=True, то при поиске должен учитываться регистр букв, иначе регистр 
# не учитывается. Функция должна возвращать кортеж вида:

# (<найденное имя>, <частота встречаемости>)

# Например, для списка:

# celebrities = ['Толстой', 'Балакирев', 'Пушкин', 'Бердяев', 'Балакирев', 'Пушкин', 'Толстой', 'пушкин']

                  
# Вызов функции:

# result = most_popular(celebrities)

                  
# должен возвращать кортеж:

# ('пушкин', 3)

# Вызовите функцию most_popular со списком writers и значением параметра case_sens равным True. 
# Результат сохраните в переменной result.

# Задачу следует реализовать, используя только текущие знания, без применения каких-либо внешних библиотек.

# P.S. На экран ничего выводить не нужно.


# здесь объявляйте функцию
def most_popular(people, *, case_sens=False):

    #people_original = people.copy()

    d = {}

    if not case_sens:
        people = [name.lower() for name in people]
        
    for name in people:
        if name not in d:
            d[name] = people.count(name)

    max_value = 0
    celeb = ''

    for name, quantity in d.items():
        if max_value < quantity:
            max_value = quantity
            celeb = name

    # for original_name in people_original:
    #     if original_name.lower() == celeb:
    #         celeb = original_name

    popular = (celeb, max_value)

    return popular


#writers = input().split()

# здесь продолжайте программу

#writers = list(writers)
writers = ['Толстой', 'Балакирев', 'Пушкин', 'Бердяев', 'Балакирев', 'Пушкин', 'Толстой', 'пушкин']

result = most_popular(writers, case_sens=True)
print(result) # убрать