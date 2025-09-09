from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

d = {'house': 'дом', 'car' : 'машина', 'tree': 'дерево', 'road': 'дорого', 'iver': 'река'}
print(d) # {'house': 'дом', 'car': 'машина', 'tree': 'дерево', 'road': 'дорого', 'iver': 'река'}

print(d['house']) # дом

d = {'house': 'дом1', 'house': 'дом2', 'house': 'дом3', 'house': 'дом4', 'house': 'дом5'}
print(d) # {'house': 'дом5'}

d = dict(one = 1, two = 2, three = '3', thour = '4', five = 5)
print(d) # {'one': 1, 'two': 2, 'three': '3', 'thour': '4', 'five': 5}

lst = [[1, 11], [2, '21'], [3, '31'], [4, 41]]
print(lst) # [[1, 11], [2, '21'], [3, '31'], [4, 41]]

d = dict(lst)
print(d) # {1: 11, 2: '21', 3: '31', 4: 41}

d[True] = 'Истина'
print(d) # {1: 'Истина', 2: '21', 3: '31', 4: 41}

d[False] = 'Ложь'
print(d) # {1: 'Истина', 2: '21', 3: '31', 4: 41, False: 'Ложь'}

d1 ={}
d1[True] = 'Истина'
print(d1) # {True: 'Истина'}
d1[True] = 'Ложь'
print(d1) # {True: 'Ложь'}
d1[False] = 'Ложь'
print(d1) # {True: 'Ложь', False: 'Ложь'}

d = {True: 1, False: 'ложь', 'list': [11, 21, 31, 41]}
print(d) # {True: 1, False: 'ложь', 'list': [11, 21, 31, 41]}
print(d['list']) # [11, 21, 31, 41]

print(len(d)) # 3

del d[True]
print(d) # {False: 'ложь', 'list': [11, 21, 31, 41]}

print('list' in d) # True
print('list99' in d) # False