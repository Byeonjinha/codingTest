import math
def solution(rows, columns, queries):

    answer = []
    map = [[(j*columns)+(i+1) for i in range(columns)] for j in range(rows)]
    for i in range(len(queries)):
        min_v = math.inf

        temp=   map [queries[i][0]-1][queries[i][1]-1]
        min_v = min(min_v,temp)

        for j in range(queries[i][0],queries[i][2]):
            map[j-1][queries[i][1]-1]=map[j][queries[i][1]-1]
            min_v = min(min_v, map[j][queries[i][1]-1])
        for j in range(queries[i][1],queries[i][3]):
            map[queries[i][2]-1][j-1]=map[queries[i][2]-1][j]
            min_v = min(min_v, map[queries[i][2]-1][j])
        for j in range(queries[i][2]-1,queries[i][0]-1,-1):
            map[j][queries[i][3]-1]=map[j-1][queries[i][3]-1]
            min_v = min(min_v , map[j-1][queries[i][3]-1])
        for j in range(queries[i][3]-1,queries[i][1]-1,-1):
            map[queries[i][0]-1][j]=map[queries[i][0]-1][j-1]
            min_v = min(min_v ,map[queries[i][0]-1][j-1])

        map[queries[i][0] - 1][queries[i][1]] = temp
        answer.append(min_v)
    return answer

rows = 100
columns = 97
quries = [[1,1,100,97]]
solution(rows,columns,quries)