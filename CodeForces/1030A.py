n = input()
a = [int(i) for i in input().split(' ')]
if sum(a):
    print('HARD')
else:
    print('EASY')