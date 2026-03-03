#  Объявите в программе функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит сообщение (без кавычек):

# "Периметр прямоугольника, равен x"
          
# где x - вычисленный периметр прямоугольника. После объявления функции прочитайте (с помощью функции input) два целых числа, 
# записанных в одну строку через пробел, и вызовите функцию с этими числовыми значениями.

# Sample Input:

# 8 11
# Sample Output:

# Периметр прямоугольника, равен 38

def calculate_rectangle_perimeter(width, height):
    print(f'Периметр прямоугольника, равен {(width+height)*2}')


width_input, height_input = map(int, input().split())
calculate_rectangle_perimeter(width_input, height_input)

