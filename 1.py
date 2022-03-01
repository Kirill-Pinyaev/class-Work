with open("17.txt") as f:
    data = list(map(int, f.readlines()))
    maxx = sum([i for i in data if abs(i) % 100 == 21])
    sp = []
    for i in range(len(data) - 2):
        if (abs(data[i]) % 10 == 7 and abs(data[i + 1]) % 10 != 7 and abs(data[i + 2]) % 10 != 7) or (
                abs(data[i]) % 10 != 7 and abs(data[i + 1]) % 10 == 7 and abs(data[i + 2]) % 10 != 7) or (
                abs(data[i]) % 10 != 7 and abs(data[i + 1]) % 10 != 7 and abs(data[i + 2]) % 10 == 7):
            if data[i] + data[i + 1] + data[i + 2] > maxx:
                sp.append(data[i] + data[i + 1] + data[i + 2])
print(len(sp))
print(max(sp))
