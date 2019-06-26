n, h = input().split()
h = int(h)
a = input().split()
a = [int(i) for i in a]
x = len([i for i in a if i>h])
print(int(n)+x)