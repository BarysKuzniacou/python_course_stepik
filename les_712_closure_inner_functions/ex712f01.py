def say_name(name):
    def say_goodbuy():
        print('don`t say me goodbuy, ' + name +'!')
    
    return say_goodbuy()


say_name('bob')
