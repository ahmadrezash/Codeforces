a = input()
a = a.split('WUB')
a = [i for i in a if i != '']
a = ' '.join(a)
print(a)