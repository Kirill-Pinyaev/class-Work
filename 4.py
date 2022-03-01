s = '5' * 125
while '55555' in s:
    s = s.replace('55555', '88', 1)
    s = s.replace('888', '555', 1)
print(s)