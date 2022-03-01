from itertools import *
s = 'БАНКИР'
data = list(product('АИ', s, s, s, s, 'АИ'))
data = [i for i in data if i.count('А') < 2 and i.count('И') < 2]
print(data)
print(len(data))