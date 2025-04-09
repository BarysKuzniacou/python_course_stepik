age = 35
name = 'Serge'
print('My name is ' + name + '. I`m ' + str(age) + '. I play football.')
print("My name is {0}. I`m {1}. I play football.".format(name, age))
print("My name is {fio}. I`m {old}. I play football. {fio}{old}".format(fio=name, old=age))
print(f'My name is {name}. I`m {age}. I play football.')
print(f'My name is {name.upper()}. I`m {age * 2}. I play football.')