import copy
def solution(land):
    temp = copy.deepcopy(land)
    answer1 = 0
    answer2 = 0
    key = -999
    for i in range(len(temp)):
        if key == temp[i].index(max(temp[i])):
            temp[i].remove(max(temp[i]))

        answer1 += max(temp[i])
        if temp[i].count(max(temp[i])) > 1:
            key = -999
        else:
            key = temp[i].index(max(temp[i]))

    land[0][land[0].index(max(land[0]))] =  -999
    for i in range(len(land)):
        if key == land[i].index(max(land[i])):
            land[i].remove(max(land[i]))
        answer2 += max(land[i])
        if land[i].count(max(land[i])) > 1:
            key = -999
        else:
            key = land[i].index(max(land[i]))
    print(answer1,answer2)
    return max(answer1, answer2)
land = [[1,2,3,5]
,[5,6,7,100]
,[4,3,2,1]]
# land = [[1,1,1,1],[2,2,2,3],[3,3,3,6],[4,4,4,7]]
solution(land)