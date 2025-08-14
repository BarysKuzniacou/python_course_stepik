def units_do_not_touch(lst_in, n):
    for i in range(0, len(lst_in)-1):
        for j in range(1, len(lst_in[i])):
            sum = lst_in[i][j-1] + lst_in[i][j] + lst_in[i+1][j-1] + lst_in[i+1][j]
            if sum > 1:
                print('test ' + str(n) + ' НЕТ')
                return 'НЕТ'

    print('test ' + str(n)+ ' ДА')

    return 'ДА'