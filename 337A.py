tmp =  input()
tmp = tmp.split()
n, m = int(tmp[0]), int(tmp[1])
a = input()
a = a.split()
a = [int(i) for i in a]
a.sort() 
a = [(a[i+n-1]-a[i]) for i in range(len(a)-n+1)]
print(min(a)) 
