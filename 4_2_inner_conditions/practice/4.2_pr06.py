# На вход программе подаются два целых числа, записанных через пробел. Необходимо прочитать эти числа по порядку в
# переменные m (порядковый номер месяца) и n (число, день месяца). Затем, по переменным m и n определить:
#
# а) дату предыдущего дня (принять, что m и n не могут являться 1 января);
# б) дату следующего дня (принять, что m и n не могут являться 31 декабря).
#
# В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd,
# где m - число месяца; d - номер дня) в одну строчку через пробел.
#
# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/4/4.2.6
#
# Sample Input:
# 8 31
# Sample Output:
# 08.30 09.01

m, n = map(int, input().split())

#---01---
if m == 1:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 12
        month_after = 1
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---02---
elif m == 2:
    if 1 < n < 28:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 28:
        day_before = 27
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 1
        month_after = 2
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---03---
elif m == 3:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 2
        month_after = 3
        day_before = 28
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---04---
elif m == 4:
    if 1 < n < 30:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 30:
        day_before = 29
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 3
        month_after = 4
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---05---
elif m == 5:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 4
        month_after = 5
        day_before = 30
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---06---
elif m == 6:
    if 1 < n < 30:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 30:
        day_before = 29
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 5
        month_after = 6
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---07---
elif m == 7:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 6
        month_after = 7
        day_before = 30
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---08---
elif m == 8:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 7
        month_after = 8
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---09---
elif m == 9:
    if 1 < n < 30:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 30:
        day_before = 29
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 8
        month_after = 9
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---10---
elif m == 10:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 9
        month_after = 10
        day_before = 30
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---11---
elif m == 11:
    if 1 < n < 30:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 30:
        day_before = 29
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 10
        month_after = 11
        day_before = 31
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')
#---12---
elif m == 11:
    if 1 < n < 31:
        day_before = n - 1
        day_after = n + 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{m:02}.{day_after:02}')
    elif n == 31:
        month_before = 12
        month_after = 1
        day_before = 30
        day_after = 1
        print(f'{m:02}.{day_before:02}' + ' ' + f'{(m + 1):02}.{day_after:02}')
    else:
        month_before = 11
        month_after = 12
        day_before = 30
        day_after = 2
        print(f'{month_before:02}.{day_before:02}' + ' ' + f'{month_after:02}.{day_after:02}')



