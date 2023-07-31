DP = [0 for i in range(91)]
for i in range(91):
    if i == 0: continue
    elif i == 1: DP[i] = 1
    else:
        DP[i] = DP[i - 1] + DP[i - 2]

print(DP[int(input())])