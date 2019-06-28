n = int(input())

tmp = input().split()
x = int(tmp[0])
xx = [int(tmp[i]) for i in range(1,len(tmp))]

tmp = input().split()
y = int(tmp[0])
yy = [int(tmp[i]) for i in range(1,len(tmp))]

if sorted(list(set().union(xx,yy))) == [i for i in range(1,n+1)]:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')