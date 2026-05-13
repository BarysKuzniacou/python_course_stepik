lst = [5, 3, 0, -6, 8, 10, 1]

def get_filter(a, filter=None):
    if filter is None:
        return a
    
    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


r = get_filter(lst)
print(r)

p = get_filter(lst, lambda x: x % 2 == 0)
print(p)

g = get_filter(lst, lambda x: x > 0)
print(g)