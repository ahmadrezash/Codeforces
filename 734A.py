i = input()
i = input()
a = i.count('A')
d = len(i) - a
if a>d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')