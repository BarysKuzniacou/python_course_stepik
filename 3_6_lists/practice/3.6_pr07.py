# put your python code here
lst_to_sort = list(map(int, input().split()))
lst = sorted(lst_to_sort, reverse=True)
print(*lst)