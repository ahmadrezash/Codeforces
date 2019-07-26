# s,n=10,2
s,n = map(int,input().split())
xy = [] #strength/improve
# y = []
from operator import itemgetter
for i in range(n):
    tmp = list(map(int,input().split()))
    xy.append(tmp)
# xy.append([1,99])
# xy.append([100,100])

def t(x):
    if x[0]<s:
        return x

res = True

while xy:
    tmp = list(map(t, xy))
    # if None in can:
    #     can.remove(None)
    can = [i for i in tmp if i] 
    if not can:
        res = False
        break

    can = sorted(can, key=itemgetter(1), reverse=True)
    tmp = can.pop(0)
    xy.remove(tmp)
    s += tmp[1]

print('YES') if res else print("NO")