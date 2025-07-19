names = ['Христофор', 'Адемар', 'Тея', 'Стефания', 'Архип']

names_starts_a = filter(lambda name: name.startswith('А'), names)

print(list(names_starts_a))