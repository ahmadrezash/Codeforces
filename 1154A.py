array = [int(i) for i in input().split(' ')]
_max = max(array)
array.remove(_max)
res = [_max-i for i in array]
print(*res)