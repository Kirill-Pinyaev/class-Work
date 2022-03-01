def f(n):
    n = bin(n)[2:]
    for i in range(3):
        if n.count('0') == n.count('1'):
            n += n[-1]
        elif n.count('0') > n.count('1'):
            n += '1'
        else:
            n += '0'
    return int(n, 2)

sp = []
print(f(225))
for i in range(500):
    a = f(i)
    if a % 4 == 0 and a % 8 != 0:
        sp.append((i, a))
print(sp)