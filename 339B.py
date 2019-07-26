n,m = map(int,input().split()) #Num of Houses #Num of Tasks
t = list(map(int,input().split())) #tasks
# print(n,m)
prev = 0
bigs = []
for i in t:
    # print(i)
    if i >= prev:
        prev = i
    else:
        bigs.append(prev)
        # print(bigs)
        prev = i
bigs.append(t[-1])
# print(bigs)
# print((len(bigs)-1)*n)
print((len(bigs)-1)*n+(bigs[-1]-1))