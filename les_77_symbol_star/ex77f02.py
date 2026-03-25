import math

def box_nd(a, b, c, *, perimeter=True, initial, **kwargs):
    if perimeter:
        return sum((a, b, c)) * 2 ** (len((a, b, c)) -1) + initial
    else:
        return math.prod(((a, b, c))) + initial
    

print(box_nd(5, c=8, b=3, initial=0))

print(box_nd(5, 7, 3, 5, 2, initial=0, verbose=True))

print(box_nd(5, 7, 3, 5, 2, initial=-1, perimeter=False))