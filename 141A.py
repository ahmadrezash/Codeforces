a,b,z = input(),input(),input()
# a = "BABBONATALE"
# b = "FATHERCHRISTMAS"
# z = "BABCHRISTMASBONATALLEFATHER"
array1 = []
array2 = []
for i in a+b:
    array1.append(i.lower())

for i in z:
    array2.append(i.lower())

if sorted(array1) == sorted(array2):
    print('YES')
else:
    print('NO')
