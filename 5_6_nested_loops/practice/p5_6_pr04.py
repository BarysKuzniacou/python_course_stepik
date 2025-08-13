# На вход программе подается двумерный список размерностью 5 х 5 элементов, состоящий из нулей и в некоторых позициях единицы (см. пример ниже). В программе уже реализовано их чтение и сохранение в списке:
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести на экран "ДА", иначе "НЕТ".
#
# Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.6.4
#
# Sample Input:
# 1 0 0 0 0
# 0 0 1 0 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# Sample Output:
# ДА

def units_do_not_touch(lst_in, n):
    for i in range(0, len(lst_in)-1):
        for j in range(1, len(lst_in[i])):
            sum = lst_in[i][j-1] + lst_in[i][j] + lst_in[i+1][j-1] + lst_in[i+1][j]
            if sum > 1:
                print('test ' + str(n) + ' НЕТ')
                return 'НЕТ'

    print('test ' + str(n)+ ' ДА')

    return 'ДА'