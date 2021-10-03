def remover(array: list):
    i = 0
    while i < len(array):
        if i + 1 < len(array) and abs(array[i] - array[i + 1]) <= 1:
            if array[i] < array[i + 1]:
                array = array[:i] + array[i + 1:]
                i = 0
            else:
                array = array[:i + 1] + array[i + 2:]
                i = 0
        else:
            i += 1
    return "YES" if len(array) == 1 else "NO"


number_of_game = int(input())

for i in range(number_of_game):
    array_len = int(input())
    new_array = list(map(lambda x: int(x), input().split(" ")))
    new_array.sort()
    print(remover(new_array))
