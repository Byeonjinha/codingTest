import sys
from itertools import combinations
N, M = list(map(int, sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
answerList = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))
chickenList = list(combinations(chicken, M))
tmpMinDistans = [0 for _ in range(len(chickenList))]
for k in range(len(chickenList)):
    for houseX, houseY in house:
        minDistance = 1000
        for chickenX, chickenY in chickenList[k]: #치킨집별 집별 간 최소 거리
            distance = abs(chickenX - houseX) + abs((chickenY - houseY))
            minDistance = min(minDistance, distance)  # 최소값으로 최신화
        tmpMinDistans[k] += minDistance
print(min(tmpMinDistans))