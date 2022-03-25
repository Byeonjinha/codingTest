# 연속된문자열 확인함수
import copy
def yunsock(list_1):
    max_count = 1

    for i in range(len(list_1)):#가로열검사
        count = 1
        for j in range(1,len(list_1[i])):
            if list_1[i][j] == list_1[i][j-1]:
                count+=1
                max_count = max(max_count,count)
            else:
                count=1
    list_2 = list(map(list, zip(*list_1)))

    for i in range(len(list_2)):#가로열검사
        count = 1
        for j in range(1,len(list_2[i])):
            if list_2[i][j] ==list_2[i][j-1]:
                count+=1
                max_count = max(max_count,count)
            else:
                count=1
    #세로열검사
    return max_count

n = int(input())   #범위입력받음
list_1 = []
max_count = 1

for i in range(n):   #범위만큼문자열받음
    m = list(input())
    list_1.append(m)



list_3 = list(map(list, zip(*list_1)))
max_count = max(yunsock(list_1),yunsock(list_3))

for j in range(len(list_1)): #가로결합
    for k in range(1,len(list_1[j])):
        list_2= copy.deepcopy(list_1)
        list_2[j][k-1],list_2[j][k] = list_2[j][k],list_2[j][k-1]
        max_count = max( max_count, yunsock(list_2))
list_3 = list(map(list, zip(*list_1)))
for j in range(len(list_3)): #세로결합
    for k in range(1,len(list_3[j])):
        list_2= copy.deepcopy(list_3)
        list_2[j][k-1],list_2[j][k] = list_2[j][k],list_2[j][k-1]
        max_count = max( max_count, yunsock(list_2))
print(max_count)
