
a = input()
# a = 'Aa'
all_caps = True

if a.isupper():
    print(a.lower())
else:
    print(a[0].upper()+a[1:].lower())