# На плоскости размером rect_width x rect_height (ширина x высота) размещены непересекающиеся 
# прямоугольники одинаковых размеров w x h, следующих друг за другом.

# Величины rect_width, rect_height, w, h читаются из входного потока следующим образом:

# rect_width, rect_height, w, h = map(int, input().split())

# Необходимо вычислить общее число прямоугольников не умещающихся целиком на плоскости. 
# Результат (количество не умещающихся прямоугольников) сохранить в переменной total.

# Программу реализовать без применения условных операторов, только используя изученный материал.

# P.S. На экран ничего выводить не нужно.

# rect_width, rect_height, w, h = map(int, input().split())

rect_width, rect_height, w, h = 640, 480, 64, 49

n_in_width = int(rect_width / w)
n_in_height = int(rect_height / h)

in_width = int(rect_width % w > 0)
in_height = int(rect_height % h > 0)

total = (n_in_width * in_height) + (n_in_height * in_width) + (in_width * in_height)
print(total)