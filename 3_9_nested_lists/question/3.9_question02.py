# Имеется многомерный список:
#
# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
#
# Какую команду следует выполнить, чтобы удалить элемент со значением "F"?

a = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]

#in a[1][2][2]
#del a[2][3][3]
#in a[1][1][2]
#del a[1][1][2]

del a[1][2][2]

print(a)