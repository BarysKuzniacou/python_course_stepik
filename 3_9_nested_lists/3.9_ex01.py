line = [1, 7, 6, 11, 3]
img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
print(img)
img = [line[:], line[:], line[:], line[:], line[:]]
print(img)
print(img[0])
print(img[0][0])
img[1] = [0, 0, 0, 0, 0]
print(img)
img[2] = [0] * 5 # формирование нового списка и замена элемента
print(img)
img[1][:] = [1] * 5 # присваивание значение
print(img)
lst1 = ["Люблю", "тебя", "Петра", "Творенье"]
lst2 = ["Люблю", "твой", "строгий", "стройный", "вид"]
lst3 = ["Невы", "державное", "теченье"]
lst4 = ["Береговой", "Её", "гранит"]
lst = [lst1, lst2, lst3, lst4]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[0][2])
lst[0][2] ='12345'
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
lst.append(["Твоих", "оград", "узор", "чугунный"])
print(lst)
del lst[1]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
lst = [[[1, 2],[True, False]],['матрица', 'вектор']]
print(lst[0])
print(lst[0][0])
print(lst[0][0][0])
