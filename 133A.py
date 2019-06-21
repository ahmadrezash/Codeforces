p = input()
o = ''
for i in p:
    if i=='H':
        o += 'Hello, World!'
    elif i=='Q':
        o += "a"
    elif i == '9':
        o += '99 Bottles of Beer'
if o == '':
    print('NO')
else:
    print('YES')