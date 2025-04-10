towns = ['Moscow', 'Minsk', 'Kiyv']
print(towns)
print(towns[0])
print(towns[1])
print(towns[2])
#print(towns[3])
print(towns[-1])
print(towns[-2])
print(towns[-3])

marks = [2, 3, 4, 3, 5, 2]
print(marks)
#print(marks/6)
marks[0] = 3
print(marks)
marks[1] = 'Minsk'
print(marks)
marks[3] = towns
print(marks)
list = list([True, False])
print(list)
print(len(list)) # длина списка - кол-во элементов
print(max(list)) # максимальное значение в списке
marks = [2, 3, 4, 3, 5, 2]
print(sum(marks)) # сумма элементов в списке
print(sorted(marks)) # сортировка списка
print(sorted(marks, reverse = True)) # сортировка по убыванию
print(sorted(towns))
print(sum(marks) / len(marks)) # нахождение среднего значения в списке
list_1 = [-1000, 2, 3]
print(min(list_1)) # минимальное значение в списке
list_2 = [4, 5]
list_3 = list_1 + list_2 # сложение списков
print(list_3)
list_4 = [1, 22, 33] * 3 # дублирование элементов списка
print(list_4)
print('Minsk' in towns) # поиск значения в списке
print([1, 2] in [1, 2, 3])
print([1, 2] in [[1, 2], 3])
print(towns)
del towns[0] # удаление элемента из списка
print(towns)
print(towns[0])
