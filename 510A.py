m,n = list(map(int,input().split()))
for i in range(1,m+1):
    if i % 2 == 1:
        print(n*'#')
    else:
        if i % 4 == 2:
            print((n-1)*'.','#',sep='')
        else:
            print('#',(n-1)*'.',sep='')
