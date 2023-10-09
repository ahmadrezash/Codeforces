tmp = input()
tmp = tmp.split()
n , k = int(tmp[0]),int(tmp[1])
tmp = input()
a = tmp.split()
a = [int(i) for i in a]
a = [i for i in a if i >= a[k-1] and i!=0]
print(len(a))
