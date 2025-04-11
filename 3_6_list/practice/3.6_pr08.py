# put your python code here
lst = list(map(str, input().split()))
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + lst
print(*lst)