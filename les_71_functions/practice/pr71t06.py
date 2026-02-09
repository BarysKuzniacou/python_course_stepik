# Объявите в программе функцию с одним параметром, которая проверяет корректность переданного ей email-адреса в виде строки. 
# Полагается, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения: 
# 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит "ДА", иначе "НЕТ".

# После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

# Sample Input:

# sc_lib@list.ru
# Sample Output:

# ДА

def check_email(email):
    symbols_email = {'0','1','2','3','4','5','6','7','8','9','_','a','e',
             'i','o','u','y','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t',
             'v','w','x','y','z','@','.'}
    
    if all(char in symbols_email for char in email) and ('@' in email and '.' in email) and ('.' in email[email.index('@'):]):
        print('ДА')
    else:
        print('НЕТ')


email_input = input().lower()
check_email(email_input)
