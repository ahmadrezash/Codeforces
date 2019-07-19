s = input()
l = sum([i.islower() for i in list(s)])
if l < len(s)-l:
    print(s.upper())
else:
    print(s.lower())