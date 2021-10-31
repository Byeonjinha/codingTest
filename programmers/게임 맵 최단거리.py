import copy
import statistics

scores2=[]
scores3=[]
scores4=[]

def solution(scores):
    answer = []
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores2.append(scores[j][i])
        scores3.append(copy.deepcopy(scores2))
        scores2.clear()
    for i in range(len(scores3)):
        if i == scores3[i].index(max(scores3[i])) and scores3[i].count(max(scores3[i]))==1    :

            scores3[i][i]='none'
        elif i== scores3[i].index(min(scores3[i])) and scores3[i].count(min(scores3[i]))==1    :
            scores3[i][i] = 'none'

    for i in scores3:
        if 'none' in i:
            i.remove('none')
            scores4.append(statistics.mean(i))
        else:
            scores4.append(statistics.mean(i))



    for i in scores4:
        if 100>=i>=90:
            answer.append('A')
        elif 90>i>=80:
            answer.append('B')
        elif 80>i>=70:
            answer.append('C')
        elif 70>i>=50:
            answer.append('D')
        elif 50>i>=0:
            answer.append('F')
    print(answer)
    return "".join(answer)

scores=[[0,0,0],[0,0,0],[0,70,0]]
solution(scores)