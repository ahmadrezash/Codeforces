s = input().split()
n, k = int(s[0]), int(s[1])
odd = (n//2)
if n%2 == 1:
    odd = odd + 1
    
if k>odd:
    k = k - odd
    print(2*k)
else:
    print(2*k-1)