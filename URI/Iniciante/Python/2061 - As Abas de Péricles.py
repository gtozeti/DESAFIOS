abas_, action_ = input().split()

abas = int(abas_)
action = int(action_)

for x in range(action):
    a = input()
    if a == 'fechou':
        abas += 1
    else:
        abas -= 1

print(abas)
