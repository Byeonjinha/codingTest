import math
from itertools import combinations
def solution(line):
    list_1 = []
    min_x = math.inf
    max_x = -math.inf
    min_y = math.inf
    max_y = -math.inf
    a =(list(combinations(line,2)))
    for i in range(len(a)):
            A = a[i][0][0]
            B = a[i][0][1]
            E = a[i][0][2]
            C = a[i][1][0]
            D = a[i][1][1]
            F = a[i][1][2]
            if (A * D - B * C) == 0:
                continue
            else:

                x = (B * F - E * D) / (A * D - B * C)
                y = (E * C - A * F) / (A * D - B * C)
            if x % 1 == 0 and y % 1 == 0:
                max_x = int(max(max_x,x))
                max_y = int(max(max_y,y))
                min_x = int(min(min_x, x))
                min_y = int(min(min_y, y))
                list_1.append([x, y])
    res = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for i in range(len(list_1)):
        res[int(list_1[i][1])-min_y][int(list_1[i][0])-min_x]="*"
    res.reverse()
    answer = []
    for j in range(len(res)):
         answer.append(''.join(res[j]))
    print(answer)
    return answer
line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
solution(line)