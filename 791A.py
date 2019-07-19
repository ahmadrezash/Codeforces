tmp = input()
tmp = tmp.split()
a = int(tmp[0])
b = int(tmp[1])
i = 0
while True:
    i += 1
    a *= 3
    b *= 2
    if a > b:
        break

print(i)