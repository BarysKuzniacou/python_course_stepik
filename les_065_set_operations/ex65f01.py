setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

# пересечение множеств
res = setA & setB
print(res) # {3, 4}

# пересечение множеств
setA &= setB
print(setA) # {3, 4}

setA = {1, 2, 3, 4}
setC = {9, 10, 11}

res = setA & setC
print(res) # set()

setA = {1, 2, 3, 4}

res = setA.intersection(setB)
print(res) # {3, 4}

setA.intersection_update(setB)
print(setA) # {3, 4}

# объединение множеств |=
setA = {1, 2, 3, 4}

res = setA | setB
print(res) # {1, 2, 3, 4, 5, 6, 7}

res = setA.union(setB) 
print(setA) 
print(res) 

# вычитание множеств
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
res1 = setA - setB
res2 = setB - setA

print(res1) # {1, 2}
print(res2) # {5, 6, 7}

setA -= setB
print(setA) # {1, 2}

# симментричная разность - уникальные элементы из множеств
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
res = setA ^ setB
print(res) # {1, 2, 5, 6, 7}

# сравнение множеств
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(setA == setB) # True
print(setA != setB) # False

setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5}

print(setA < setB) # False
print(setA > setB) # True

setB.add(22)

print(setA < setB) # False
print(setA > setB) # False

setA = {7, 6, 5, 4, 3}
setB = {7, 6, 5, 4, 3}
print(setA < setB) # False
print(setA > setB) # False

print(setA <= setB) # True
print(setA >= setB) # True
