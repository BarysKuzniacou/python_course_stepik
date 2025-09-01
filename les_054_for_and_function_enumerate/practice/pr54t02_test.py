# На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке:
#
# +7(xxx)xxx-xx-xx
#
# где x - это любая цифра. Число введенных символов считается верным (то есть, не может быть, чтобы отсутствовала
# какая-либо цифра или была лишняя). Необходимо прочитать строку из входного потока и проверить, что она содержит
# номер телефона в соответствии с приведенным форматом. Вывести "ДА", если это так и "НЕТ" в противном случае.
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.2
# test #1
# input: +7(123)456-78-99
# output: ДА
# test #2
# input: +7 123-456-78-99
# output: НЕТ
# test #3
# input: -7(123)456-78-99
# output: НЕТ
# test #4
# input: +7(aaa)345-78-99
# output: НЕТ
# test #5
# input: +7(123)-6f-66-77
# output: НЕТ
# test #6
# input: +7(123)656-66-77
# output: ДА
# test #7
# input: +8(123)656-66-77
# output: НЕТ
# test #8
# input: +7(123)656 66-77
# output: НЕТ
# test #9
# input: +7(123)656-66 77
# output: НЕТ
# test #10
# input: +7(123)656-aa-77
# output: НЕТ
# test #11
# input: +7(1!3)656-66-77
# output: НЕТ
# test #12
# input: +7(xxx)xxx-xx-xx
# output: НЕТ
# Sample Input:
# +7(123)456-78-99
# Sample Output:#
# ДА

# +7(xxx)xxx-xx-xx

def is_phone_number(number):

    lst_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if number[0] != '+':
        return False

    if number[1] != '7':
        return False

    if number[2] != '(' or number[6] != ')':
        return False

    if number[10] != '-' or number[13] != '-':
        return False

    if (number[3] not in lst_nums or number[4] not in lst_nums or number[5] not in lst_nums or
            number[7] not in lst_nums or number[8] not in lst_nums or number[9] not in lst_nums or
            number[11] not in lst_nums or number[12] not in lst_nums or
            number[14] not in lst_nums or number[15] not in lst_nums):
        return False

    return True

data_lst = ['+7(123)456-78-99', '+7 123-456-78-99', '-7(123)456-78-99', '+7(aaa)345-78-99', '+7(123)-6f-66-77',
            '+7(123)656-66-77', '+8(123)656-66-77', '+7(123)656 66-77', '+7(123)656-66 77', '+7(123)656-aa-77',
            '+7(1!3)656-66-77', '+7(xxx)xxx-xx-xx']

result = ['ДА', 'НЕТ', 'НЕТ', 'НЕТ', 'НЕТ',
          'ДА','НЕТ', 'НЕТ', 'НЕТ', 'НЕТ',
          'НЕТ', 'НЕТ']

i = 0

for data in data_lst:
    phone_number = is_phone_number(data)
    if phone_number:
        print(data, " -> ДА", result[i])
        i += 1
    else:
       print(data, " -> НЕТ", result[i])
       i += 1