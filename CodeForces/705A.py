n = int(input())
a = [("I love that" if i%2 else 'I hate that') for i in range(n)]
a[-1] = a[-1].replace('that','it')
print(' '.join(a))