# В программе выполняется чтение двумерного списка чисел размером n x m элементов:

# s = sys.stdin.readlines()
# lst2D = [list(map(int, x.strip().split())) for x in s]
               
# Формат списка lst2D следующий (пример):

# lst2D = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
            
# Необходимо перебрать элементы этого списка змейкой, т.е. в порядке, показанном на рисунке и 
# последовательно вывести их на экран в одну строчку через пробел:
# 1 2 3 4 5 6 7 8 9

# import sys
# s = sys.stdin.readlines()
# lst2D = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу

lst2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst = []

for i, d in enumerate(lst2D):
    if i % 2 == 0:
        lst.append(d)
    else:
        lst.append(d[::-1])