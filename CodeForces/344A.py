n = input()
n = int(n)
a = []

for i in range(n):
    a.append(input())

a = ''.join(a)

f = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        f += 1  
print(f)

