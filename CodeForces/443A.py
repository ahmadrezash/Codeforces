a = input()
a = a.replace(' ','').replace('{','').replace('}','').split(',')
if a[0] == '':
    print(0)
else:
    print(len(set(a)))
