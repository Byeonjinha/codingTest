N = int(input())
name = []
player = []
for i in range(N):
    name.append(input())
for i in name:
    count = 0
    for j in name:
        if i[0] == j[0]:
            count+=1
    if count >=5:
        player.append(i[0])
if len(player) == 0 :
    print("PREDAJA")
else:
    print(''.join(sorted(list(set(player)))))