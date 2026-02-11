# Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет, 
# можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина любой его 
# стороны должна быть меньше суммы двух других). Если  проверка проходит, функция должна возвращать булево 
# значение True, а иначе False.

# Вызывать функцию не нужно, только объявить.

# Sample Input:

# 3 4 5
# Sample Output:

# True

def is_triangle(a, b, c):
    return True if a < (b + c) and b < (a + c) and c < (a + b) else False

# def is_triangle(a, b, c):
#     a, b, c = sorted((a, b, c)) # в скобках кортеж 
#     return c < a + b

# def is_triangle(a, b, c):
#     return a < b + c and b < a + c and c < a + b

# def is_triangle(a, b, c):  
#     return 2 * max(a, b, c) < a + b + c

# def is_triangle(*args):
#     return max(args) < (sum(args) - max(args))