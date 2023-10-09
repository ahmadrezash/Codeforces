n = int(input())
a = input().split()
a = [int(i) for i in a]
a.sort()
a = [str(i) for i in a]
print(' '.join(a))