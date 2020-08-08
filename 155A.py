a = input()
l = [int(i) for i in input().split()]
print(len(list(filter(lambda x:True if x>0 else False ,[l[i+1]-l[i] for i in range(len(l)-1)]))))

# print(l)
# l2 = [l[i+1]-l[i] for i in range(len(l)-1)]
# print(l2)
# x = list(filter(lambda x:True if x>0 else False ,l2))
# print(x)
# print(len(x))
