def sum_ar(n, a0=0, d=1, acc=0):
    if n <= 1:
        print(a0)
        return acc + a0

    print(a0 + (n-1)*d, end =', ')
    return sum_ar(n-1, a0, d, acc + a0 + (n-1)*d)


res = sum_ar(5, 2, 3)
print(res)