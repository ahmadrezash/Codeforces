n = int(input())

all = [int(i) for i in input().split()]

import math
# import sympy

# def is_prime(n):
#     n = abs(int(n))
#     if n < 2:
#         return False
#     if n == 2: 
#         return True    
#     if not n & 1: 
#         return False
#     for x in range(3, int(n**0.5) + 1, 2):
#         if n % x == 0:
#             return False
#     return True
is_prime = lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])
def is_T_Prime(x):
    flag = False
    xx = int(math.sqrt(x))
    if xx**2 == x and is_prime(xx):
        if x is not 1:
            flag = True
    if flag:
        print('YES')
    else:
        print('NO')

for i in all:
    is_T_Prime(i)
