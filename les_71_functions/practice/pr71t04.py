#  Объявите в программе функцию, которая в качестве параметра принимает список (list), находит максимальное, минимальное и сумму значений 
# этого списка и выводит результат на экран в виде строки (без кавычек):

# "Min = v_min, max = v_max, sum = v_sum"

                  
# где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.

# После объявления функции прочитайте (с помощью функции input) список целых чисел, записанных в одну строку через пробел, и вызовите функцию с передачей ей этого списка.

# Sample Input:

# 8 11 5 -10 12 0
# Sample Output:

# Min = -10, max = 12, sum = 26

def max_min_sum_list(lst):
    v_max = max(lst)
    v_min = min(lst)

    v_sum = 0

    for i in range(len(lst)):
        v_sum += lst[i]
    
    print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')


lst_input = list(map(int, input().split()))

max_min_sum_list(lst_input)