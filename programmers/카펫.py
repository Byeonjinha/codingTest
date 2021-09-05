from itertools import combinations
def solution(brown, yellow):
    list1=[]
    list2=[]

    for i in range(1,5001):
        for j in range(1,5001):
            if i*j==yellow:
                list1.append([i,j])
    for i in range(len(list1)):
        if brown==2*list1[i][0]+2*list1[i][1]+4:
            list2.append([list1[i][0]+2,list1[i][1]+2])
    list2.sort(key=lambda x:-x[0])
    answer = list2[0]
    return answer

brown=24
yellow=24

solution(brown, yellow)