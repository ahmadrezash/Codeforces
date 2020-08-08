n, k = (int(i) for i in input().split(' '))

tmp = n

for i in range(k):
    if tmp%10 == 0:
        tmp/=10
    else:
        tmp-=1
print(int(tmp))