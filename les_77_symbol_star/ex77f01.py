import math

def box_nd(a, b, c, *args, perimeter=True):
    if perimeter:
        return sum((a, b, c, *args)) * 2 ** (len((a, b, c, *args)) -1)
    else:
        return math.prod(((a, b, c, *args)))
    

print(box_nd(5, 7, 3))

print(box_nd(5, 7, 3, 5, 2))

print(box_nd(5, 7, 3, 5, 2, perimeter=False))