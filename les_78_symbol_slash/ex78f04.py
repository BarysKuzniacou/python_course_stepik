def rect(width, height, /, offset, *, perrimeter=True, **kwargs):
    if perrimeter:
        return (width + height) * 2 + offset
    else:
        return (width * height) + offset
    

res1 = rect(10, 20, 0)
print(res1)

res2 = rect(10, 20, perrimeter=False, offset=5)
print(res2)

res3 = rect(10, 20, 10, perrimeter=False)
print(res3)
