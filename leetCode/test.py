import re


def funca(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = funca(n - 2) + funca(n - 1)
    print('----', n, result)
    return result


def funcb(n):
    s1 = 1
    s2 = 2
    for i in range(3, n + 1):
        s1, s2 = s2, s1 + s2
        print(i, s2)
    return s2


# funca(10)

# print('=====' * 20)
# funcb(10)


def is_odd(n):
    return n % 2 == 1


tt = filter(is_odd, [0, 1, 2, 3, 4, 5, 6])
print(list(tt))


def is_digit(s):
    return re.match(r'[\d\.]', s) is not None


def is_alpha(s):
    return re.match(r'[a-zA-Z]', s) is not None


# ss = "Colour Temperature is 27.00 Kelvin"
# ss1 = filter(is_digit, ss)
# print(''.join(ss1))
# ss2 = filter(is_alpha, ss)
# print(''.join(ss2))

strs = ['flight', 'fliw', 'fliwer']
print(min(strs))
print(max(strs))
for i in zip(*strs):
    print(i)
    # print(set(i))

x = [1, 2, 3]
y = [4, 5]
z = [7, 8, 9, 10]
xyz = zip(x, y, z)
print(xyz)
for i in xyz:
    print(i)

x = ['a', 'b', 'c']
y = ['x', 'y', 'z']

d = zip(x, y)
d = dict(d)
print(d)

a = [1, 2, 3, 4, 5, 6]
b = zip(*([iter(a)] * 3))
print(*[iter(a)])
print(b)
for i in b:
    print(i)
