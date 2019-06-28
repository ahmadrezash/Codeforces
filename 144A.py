n = int(input())
a = input().split()
a = [int(i) for i in a]


m = min(a)
x = max([i for i,val in enumerate(a) if val==m])
n1 = len(a) - (x+1)
a.pop(x)
a.append(m)


m = max(a)
x = min([i for i,val in enumerate(a) if val==m])
n2 = x

a.pop(x)
a = [m]+a

print(n1+n2)
