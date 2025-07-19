names = ['Христофор', 'Адемар', 'Тея', 'Стефания', 'Архип']

names_starts_a = []

for name in names:
    if name.startswith('А'):
        names_starts_a.append(name)

print(names_starts_a)

names_starts_a2 = [name for name in names if name.startswith('А')]

print(names_starts_a2)

