n = int(input())

s = input()
s = s.split()
s = [int(i) for i in s]
s_1,s_2,s_3,s_4 = s.count(1),s.count(2),s.count(3),s.count(4)

#STEP 1
c = s_4

#STEP 2
tmp = min(s_1,s_3)
c = c + tmp

s_1 -= tmp
s_3 -= tmp

#STEP 3
tmp = s_2//2
c = c + tmp

s_2 -= 2*tmp

#STEP 4
if s_1 == 0 and s_2 == 0 and s_3 == 0:
    print(c)
elif s_1 == 0 and s_2  > 0 and s_3 == 0:
    print(c+1)
elif s_3 > 0 and s_2 == 0:
    print(c+s_3)
elif s_1 > 2:
    s_1 -= 2*s_2
    if s_1 % 4 != 0:
        c += s_1//4 + 1
    else :
        c += s_1//4
    print(c+s_2)
elif s_1 <= 2 and s_1 > 0:
    print(c + 1)
elif s_3 > 0 and s_2 > 0:
    print(c+1+s_3)

