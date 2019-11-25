def funca(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = funca(n-2) + funca(n-1)
    print('----', n, result)
    return result


def funcb(n):
    s1 = 1
    s2 = 2
    for i in range(3, n+1):
        s1, s2 = s2, s1+s2
        print(i, s2)
    return s2


funca(10)

print('====='*20)
funcb(10)


