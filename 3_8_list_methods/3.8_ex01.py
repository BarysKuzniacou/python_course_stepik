lst01 = [1, -54, 3, 23, 43, -45, 0]

# добавление в конец списка. меняется также сам список
lst01.append(100)
print(lst01)

lst01 = lst01.append(40)
print(lst01)

lst01 = [1, -54, 3, 23, 43, -45, 0]

lst01.append(True)
print(lst01)

lst01.append(["one", 'two', 'three'])
print(lst01)

#вставка в список в определенное место значения
lst01.insert(3, -1000)
print(lst01)

# удаление значения из списка
print('добавляем ещё одно True и Fales')
lst01.append(True)
lst01.append(False)
print(lst01)
print('удаляем True')
lst01.remove(True) # булевые значения приводятся к числовым значениям
                   # в данном случае будет удален первый элемент, т.к. True = 0
                   # False = 0
lst01.remove(False)
print(lst01)
print('Повторно удаляем удаляем True и False')
lst01.remove(True) # Удаляется первый найденный True
lst01.remove(False)
print(lst01)
#lst01.remove('one')
# print('remave one', lst01) # ошибка при удалении значения во вложенном списоке
# lst01.remove(55)
# print('remave one', lst01) # ошибка при попытке удаления несуществующего значения

#удаление последнего элемента
popRemove = lst01.pop()
print('удаленный элемент', popRemove)
print('список', lst01)
popRemove = lst01.pop()
print('удаленный элемент', popRemove)
print('список', lst01)

# удаление элемента по индексу
lst01.pop(3)
print('список после удлаления элемента под индексом 3', lst01)

# pop удаляет элемент по индексу, remove - по значению

# удаление всех значений/элементов из списка
lst01.clear()
print(lst01)

lst01 = [1, -54, 3, 23, 43, -45, 0]

# создание копии списка
lst02 = lst01.copy()
print('lst02:', lst02)
print('lst01 id:', id(lst01))
print('lst02 id:', id(lst02))

# count - считает количество значений
lst02.append(1)
print(lst02.count(1))

# index определение индекса значения
print(lst01, '-54 под индексом', lst01.index(-54))

# reverse
print('reverse')
lst02.reverse()
print(lst02)

# sort
lst02.sort()
print(lst02)
lst02.sort(reverse=True)
print(lst02)
print(sorted(lst02)) # отличие sort от sorted, sort меняет список и ничего не возвращает
print(lst02)


