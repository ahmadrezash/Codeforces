a = input()
a = [ i=='4' or i=='7' for i in a]
if sum(a) == 4 or sum(a) == 7 :
    print('YES')
else:
    print('NO')