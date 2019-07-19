tmp = input().split()
a, b = int(tmp[0]), int(tmp[1])
# a, b = 2,1
a1 = a
b1 = b
# print(a,b)
for i in range(min(a,b)):
    a1 -= 1
    b1 -= 1
    # print(a1,b1,'    ' ,i)
    if (a1==0 or b1==0):
        break

if i % 2 != 0:
    print('Malvika')
else:
    print('Akshat')