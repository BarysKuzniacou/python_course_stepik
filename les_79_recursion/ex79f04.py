def fact(n, a=1):
    if n <= 1:
        return a

    return fact(n-1, a * n)


res = fact(3)

print(res)