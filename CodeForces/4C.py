n = int(input())
# n=2
users = dict()
for i in range(n):
    new_user = input()
    # print(new_user in users.keys())
    if not new_user in users.keys():
        print('OK')
        users[new_user]=0
    else:
        users[new_user] += 1
        print(f'{new_user}{users[new_user]}')