s = input()
s = int(s)
a = s//5
b = (s-5*a)//4
c = (s-5*a-4*b)//3
d = (s-5*a-4*b-3*c)//2
e = (s-5*a-4*b-3*c-2*d)//1

print(a + b + c + d + e)