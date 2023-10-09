n = int(input())
h = []
g = []
for i in range(n):
    tmp = input()
    tmp = tmp.split()
    h.append(tmp[0])
    g.append(tmp[1])

s = 0
for i in g:
    s = s + h.count(i)

print(s)

