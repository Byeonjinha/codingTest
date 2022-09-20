import copy
from collections import defaultdict
answer = []
def dfs(dicTickets, start,answerList):
    global answer
    check = True
    def removeDestination(dicTickets, start, endIndex):
        dicTickets[start].pop(endIndex)
        return dicTickets
    for i in range(len(dicTickets[start])):
        dicTickets2 = copy.deepcopy(dicTickets) # deepcopy해야 리스트 누적삭제가 안돼요.
        answerList2 = copy.deepcopy(answerList)
        answerList2.append(dicTickets[start][i])
        dfs(removeDestination(dicTickets2,start,i), dicTickets[start][i],answerList2)
    for k in dicTickets:
        if len(dicTickets[k]) > 0 :
            check = False
    if check:
        answer.append(answerList)
def solution(tickets):
    global answer
    dicTickets = defaultdict(list)
    for i in tickets:
        dicTickets[i[0]].append(i[1])
    for j in dicTickets:
        dicTickets[j].sort()
    dfs(dicTickets, "ICN",["ICN"])
    return answer[0]