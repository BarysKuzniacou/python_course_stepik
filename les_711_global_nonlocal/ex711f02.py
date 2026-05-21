x = 100

def outer():
    x = 200
    
    def inner():
        nonlocal x # comment this
        x = 300
        print('inner ', x)
    
    inner()
    print('outer ', x)


print('global', x)
outer()