def add_value(value, lst=[]):
    lst.append(value)
    return lst


l = add_value(1)
l = add_value(2)
print(l) # [1, 2]