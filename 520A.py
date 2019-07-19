n = int(input())
s = input()
s = s.lower()
a = []
for i in s:
    a.append(i)
if len(set(a)) == 26:
    print('YES')
else:
    print('NO')

print()