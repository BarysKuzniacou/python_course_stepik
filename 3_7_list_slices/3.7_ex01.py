lst01 = ['Minsk', 'Mogilev', 'Gomel', 'Grodno', 'Vitebsk', 'Brest']
lst02 = lst01[1:4] # 'Minsk', 'Mogilev', 'Gomel', 4 не включается
print(lst02)
lst02[0] = 'Byhov'
print(lst02)
print(lst01)
print(lst01[1:])
print(lst01[:3])
lst03 = lst01[:] # создается копия списка - Вариант 1
lst04 = lst01 # список один
print(id(lst01))
print(id(lst03))
print(id(lst04))
lst04[1] = 'Berlin' # т.к. ссылка на один список, то изменение актуально и для lst01
print(lst01)
print(lst04)
lst05 = list(lst01) # создается копия списка - Вариант 2
print(id(lst01))
print(id(lst05))
lst06 =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('(lst06[1:-1]', lst06[1:-1]) # 1-9
print(lst06[2:5:2]) # переборка элементов списка с шагом
print(lst06[::-2]) # переборка элементов списка в обратном порядке с шагом
lst06[5:7] = ['Five', 'Six']
print(lst06)
lst06[5:7] = True, False
print(lst06)
# сравнение списков
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] != [1, 2, 3])
print([1, 2, 3] < [1, 2, 3])
print([1, 200, 300] < [10, 2, 3]) # идет сравнение по элементам. как только первый элемент становится не равным, то
                                  # возвращается соответствующее значение и остальные элементы не сравниваются
print([1, 1, 1, 1] < [10, 2, 3]) # идет сравнение по элементам. даже элементов в списке больше, идет сравнение до
                                 # первого неравного
print([1, 2, 3, "4"] > [1, 2, 3, "5"])
print(ord("4"), ord("5"))
