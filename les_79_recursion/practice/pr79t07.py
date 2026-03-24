# На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и 
# сохранить в списке. Затем, выполнить сортировку этого списка по возрастанию с помощью 
# алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.

# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат 
# на экран в виде последовательности чисел, записанных через пробел.

# Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.

# P. S. Теория сортировки в видео предыдущего шага.

# Sample Input:

# 8 11 -6 3 0 1 1
# Sample Output:

# -6 0 1 1 3 8 11

# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC

def comparison(left, right):
    res = []

    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left or right)

    return res

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
        
    mid = int(len(lst)/2)

    lst_left = lst[:mid]
    lst_right = lst[mid:]

    lst_left = merge_sort(lst_left)
    lst_right = merge_sort(lst_right)

    return comparison(lst_left, lst_right)

        
lst_in = list(map(int, input().split()))# [8, 11, -6, 3, 0, 1, 1]

print(*merge_sort(lst_in))