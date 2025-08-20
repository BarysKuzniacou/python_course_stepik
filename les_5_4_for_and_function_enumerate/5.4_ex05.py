t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'ts', 'ch', 'sh',
     'shch', '\"', 'y', '\'', 'e', 'yu', 'ya']

start_index = ord('а')

title = 'Программирование на Python - лучший курс'

slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s)-start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s == " !?;:.,*":
        slug += '-'
    else:
        slug += s

print(slug)