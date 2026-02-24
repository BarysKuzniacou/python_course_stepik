# В функцию из предыдущего подвига 5 добавьте в конец еще один третий параметр up с начальным булевым значением True. 
# Если параметр up равен True, то тег, указанный в параметре tag, следует записывать заглавными буквами, а иначе малыми.

# После объявления функции далее в программе прочитайте из входного потока строку и дважды вызовите функцию (с выводом результата ее работы на экран):

# первый раз со строкой и именованным аргументом tag со значением 'div';
# второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.

# Sample Input:

# Python is the best!
# Sample Output:

# <DIV>Python is the best!</DIV>
# <div>Python is the best!</div>

def tag_html(str, tag='h1', up=True):
    tag = tag.upper() if up == True else tag.lower()
    return f'<{tag}>{str}</{tag}>'


intput_str = input()

print(tag_html(intput_str, 'div'))
print(tag_html(intput_str, 'div', False))