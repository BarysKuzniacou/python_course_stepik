def add_value(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


l1 = add_value(1)
l2 = add_value(2)
l3 = add_value(3)
l3 = add_value(4, l3)
print(l1) # [1]
print(l2) # [2]
print(l3) # [3, 4]