n,d = list(map(int,input().split()))
lantern = list(map(int,input().split()))
lantern.sort() 
tmp = []
if len(lantern) == 1:
    print(max((lantern[0]-0),(d-lantern[0])))
else:
    for i in range(len(lantern)-1):
        tmp.append(lantern[i+1]-lantern[i])
    print(max(max(tmp)/2,lantern[0]-0,d-lantern[-1]))