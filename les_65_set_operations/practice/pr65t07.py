# На вход программе подается натуральное число, которое может содержать только 
# простые множители 1, 2, 3, 5 и 7 (любые из них, не обязательно все). Необходимо 
# прочитать это число и разложить его на простые множители. Затем, проверить, 
# содержит ли оно множители 2, 3 и 5 (обязательно все их, хотя бы один раз). 
# Если это так, то вывести "ДА", иначе "НЕТ".

# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.5.7

# Sample Input:
# 210
# Sample Output:
# ДА

n = int(input())

mult = 2
s_mult_res = set()

s_mult_requirement = {2, 3, 5}

while (n > 1):

    while n % mult == 0:
        s_mult_res.add(mult)
        n = n / mult
    
    mult += 1

if (s_mult_res >= s_mult_requirement):
    print('ДА')
else:
    print('НЕТ')