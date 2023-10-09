a,b = (int(i) for i in input().split())

res = 0
res = a

while (a >= b):
    res += a//b
    a = a//b
print(res)