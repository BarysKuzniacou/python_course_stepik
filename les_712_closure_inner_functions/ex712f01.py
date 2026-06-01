def say_name(name):
    def say_goodbye():
        print('don`t say me goodbuy, ' + name +'!')
    
    return say_goodbye


f = say_name('bob')
f2 = say_name('python')
f()
f2()
