import math
def solution(N, road, K):
    answer = 0-
    distance = [math.inf for _ in range(N+1)]
    print(distance)
    for i in range(len(road)):
        print(road[i])
        if road[i][0] == 1:
            print("a")
            if distance[road[i][1]] > road[i][2]:
                distance[road[i][1]] = road[i][2]
        else:
            length = 0


            if distance[road[i][1]] > road[i][2]+:

    print(distance)


    return answer

N= 5
road= [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K	= 3
solution(N, road, K)