# Продолжите программу, в которой определены следующие переменные:

# DEBUG = 10, 'DEBUG'
# INFO = 20, 'INFO'
# WARNING = 30, 'WARNING'
# ERROR = 40, 'ERROR'
# CRITICAL = 50, 'CRITICAL'

                  
# После них нужно объявить функцию с именем log_event со следующими параметрами (порядок важен):

# timestamp - временная метка лога (целое число); только позиционные аргументы;
# message - текст сообщения лога (строка); только позиционные аргументы;
# level=INFO - уровень сообщения лога; только именованные аргументы;
# format_log="[%(time)] %(levelname) - %(message)" - формат сообщения лога; только именованные аргументы.
# Функция log_event должна формировать и возвращать строку лога, если уровень сообщения level от INFO и выше (по числовому значению), а иначе возвращать None. Строка лога должна формироваться в соответствии с заданным форматом format_log. Эта форматная строка может содержать следующие спецификаторы:

# %(time) - на ее место должна подставляться временная метка timestamp;
# %(message) - на ее место должен подставляться текст сообщения message;
# %(levelname) - на ее место должно подставляться имя уровня сообщения ('DEBUG', 'INFO' и т.п.);
# %(levelno) - на ее место должно подставляться числовое значение уровня сообщения (10, 20 и т.д.).
# Например:

# res1 = log_event(1764230394, 'Сервер приложения запущен')
# res2 = log_event(1764230425, 'Медленный GET-запрос', level=WARNING)
# res3 = log_event(1764230410, 'Ошибка подключения к БД', level=ERROR,
#                  format_log="%(levelno), %(time): %(message)")

# # res1: [1764230394] INFO - Сервер приложения запущен
# # res2: [1764230425] WARNING - Медленный GET-запрос
# # res3: 40, 1764230410: Ошибка подключения к БД

                  
# Вызовите функцию log_event со следующими аргументами:

# log_time = int(input())
# log_msg = input()

                  
# уровень сообщения WARNING;
# формат сообщения: "%(levelname) - (%(time)) %(message)"
# Результат, возвращенный функцией log_event, сохраните в переменной log_item.

# P.S. На экран ничего выводить не нужно.

# значения этих переменных в программе не менять
DEBUG = 10, 'DEBUG'
INFO = 20, 'INFO'
WARNING = 30, 'WARNING'
ERROR = 40, 'ERROR'
CRITICAL = 50, 'CRITICAL'

# здесь объявляйте функцию
def log_event(timestamp, message, /, *, level=INFO, 
              format_log="[%(time)] %(levelname) - %(message)"):
    
    if level < INFO:
        return None
    
    text_log = format_log[:]

    if '%(time)' in format_log:
        text_log = text_log.replace('%(time)', str(timestamp))

    if '%(message)' in format_log:
        text_log = text_log.replace('%(message)', message)
    
    if '%(levelname)' in format_log:
        text_log = text_log.replace('%(levelname)', level[1])
    
    if '%(levelno)' in format_log:
        text_log = text_log.replace('%(levelno)', str(level[0]))
    
    return text_log


res1 = log_event(1764230394, 'Сервер приложения запущен')
print(res1) # res1: [1764230394] INFO - Сервер приложения запущен
res2 = log_event(1764230425, 'Медленный GET-запрос', level=WARNING)
print(res2) # res2: [1764230425] WARNING - Медленный GET-запрос
res3 = log_event(1764230410, 'Ошибка подключения к БД', level=ERROR,
                 format_log="%(levelno), %(time): %(message)")
print(res3) # res3: 40, 1764230410: Ошибка подключения к БД

# log_time = int(input())
# log_msg = input()

# log_time = int(input())
# log_msg = input()

# # # здесь продолжайте программу
# log_item = log_event(log_time, log_msg, level=WARNING, 
#                      format_log="%(levelname) - (%(time)) %(message)")