from collections import deque
def solution(startNumber, endNumber):

    sujja_list = deque(['0']*10)
    sujja_list2 = []
    if startNumber < endNumber:
        for i in range(0,10):
            if startNumber > endNumber:
                break
            sujja_list.append(str(startNumber))
            sujja_list.popleft()
            sujja_list2.append(''.join((list(sujja_list))))
            startNumber+=1

    elif startNumber > endNumber:
        for i in range(0,10):
            if startNumber < endNumber:
                break
            sujja_list.append(str(startNumber))
            sujja_list.popleft()
            sujja_list2.append(''.join((list(sujja_list))))
            startNumber-=1



    answer = sujja_list2
    print(sujja_list2)
    return answer


startNumber=9
endNumber=1
solution(startNumber,endNumber)