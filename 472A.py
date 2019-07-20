a = int(input())
import math  


def is_prime(num):
    is_prime = True
    for i in range(2, int(math.sqrt(num))+1): 
        if (num % i) == 0: 
            is_prime = False
            break
    
    return(is_prime)

for i in range(4,a+1):
    if not is_prime(i) and not is_prime(a-i):
        print(i,a-i)
        break