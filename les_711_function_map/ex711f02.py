b = map(int, ['1', '2', '3', '5', '7'])
b_sum = sum(b)
print(b_sum)

c = (int(x) for x in ['1', '2', '3', '5', '7'])
c_list = list(c)
print(c_list)
c_sum = sum(c)
print(c_sum)


d = map(int, ['1', '2', '3', '5', '7'])
d_sum = sum(d)
print(d_sum)