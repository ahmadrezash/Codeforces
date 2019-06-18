import math
n = int(input())
even = n//2 
odd  = n - even

sum_even = even*(even+1)
sum_odd  = odd*(2+(odd-1*2))

print(sum_even - sum_odd)


