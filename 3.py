data = 18 ** 105 + 25 * 16 ** 100 - 3 ** 51
sp = [0] * 13
while data:
    sp[data % 13] += 1
    data //= 13
print(sp[12])