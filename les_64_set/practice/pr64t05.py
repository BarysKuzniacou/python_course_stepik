# В аккаунте YouTube Сергея прокомментировали очередное видео. Некоторые посетители 
# оставляли несколько комментариев. Требуется по списку комментариев определить 
# уникальное число комментаторов (полагается, что имена у разных комментаторов не совпадают). 
# Комментарии поступают на вход программе в формате:

# имя 1: комментарий 1
# имя 2: комментарий 2
# ...
# имя N: комментарий N

# В программе уже реализовано считывание этих строк и сохранение в списке:

# lst_in = list(map(str.strip, sys.stdin.readlines()))

                  
# Выведите на экран общее число уникальных комментаторов.

# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.4.7

# Sample Input:
# EvgeniyK: спасибо большое!
# LinaTroshka: лайк и подписка!
# Sergey Karandeev: крутое видео!
# Евгений Соснин: обожаю
# EvgeniyK: это повтор?
# Sergey Karandeev: нет, это новое видео
# Sample Output:
# 4

lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 
          'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 
          'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']

s = set()

for comment in lst_in:
    index = comment.index(':')
    s.add(comment[:index])

print(len(s))

# print(len(set(i.split(":")[0] for i in lst_in )))