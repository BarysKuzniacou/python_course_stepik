# записать в список квадраьты от 1 до n, если квадраты меньше n
n = 10

lst = [b for x in range(n) if (b := x * x) < n]

print(lst)