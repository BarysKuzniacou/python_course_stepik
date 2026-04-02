# Выберите все верные утверждения, касающиеся следующей программы:

def symbol_upper(msg, indx=0, *, ignore_indx, to_upper=True):
    if indx in ignore_indx:
        return msg

    new_char = msg[indx].upper() if to_upper else msg[indx].lower()
    msg = msg[:indx] + new_char + msg[indx+1:]

    return msg


res1 = symbol_upper("Python is the best language.", ignore_indx=(3, 6))
res2 = symbol_upper("Python is the best language.", 2, ignore_indx=(3, 6))
res3 = symbol_upper("Python is the best language.", 3, (3, 6))


# параметр ignore_indx в объявлении функции symbol_upper() должен иметь значение по умолчанию, т.к. 
# перед ним записан параметр indx=0 с начальным значением

# при объявлении функции все параметры после символа * должны иметь начальные значения

# V переменная res2 будет ссылаться на строку "PyThon is the best language."

# V третий вызов функции symbol_upper с формированием значения res3 приведет к ошибке