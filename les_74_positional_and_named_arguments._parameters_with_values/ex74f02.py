def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    
    return s1 == s2


print(cmp_str('Python ', ' PYthon', reg=True))