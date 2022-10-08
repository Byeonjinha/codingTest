import sys
from itertools import combinations
from itertools import permutations
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
index = [i for i in range(N)]
totalTeam = set(index)
answer = 100000000
for i in list(combinations(index, N//2)):
    Ateam = i
    AteamPoint = 0
    BteamPoint = 0
    Bteam = tuple(totalTeam - set(Ateam))
    AteamPermutations = permutations(Ateam, 2)
    BteamPermutations = permutations(Bteam, 2)
    for i2, j2 in AteamPermutations:
        AteamPoint += graph[i2][j2] + graph[j2][i2]
    for i3, j3 in BteamPermutations:
        BteamPoint += graph[i3][j3] + graph[j3][i3]
    answer = min(answer, abs(AteamPoint - BteamPoint))
print(answer//2)
