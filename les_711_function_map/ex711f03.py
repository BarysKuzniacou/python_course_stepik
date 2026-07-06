cities = ['Minsk', 'London', 'Cherepovets']
b = map(len, cities)
print(list(b))

u = map(str.upper, cities)
print(list(u))

def symbols(s):
    return list(s.lower())


f = map(symbols, cities)
print(list(f))

lambda_f = map(lambda s: list(s.lower()), cities)
print(list(lambda_f))
