import copy
import sys
T = int(sys.stdin.readline())
list1 = []
list2 = []
list3 = []
def rooms(H,W):
    list1.clear()
    list2.clear()
    list3.clear()
    for h in range(1,H+1):
        for w in range(1,W+1):
            w = str(w)
            h = str(h)
            if int(w) < 10 :
                w="0"+w
            sum=h+w
            list1.append(sum)
        list2.append(copy.deepcopy(list1))
        list1.clear()
    for node in list(zip(*list2)):
        list3.append(node)

    return list3


def solution(T):
    for i in range(0,T):
        H,W,N= map(int, sys.stdin.readline().split())
        for x in rooms(H,W):
            for y in x:
                N-=1
                if N==0:
                    print(y)
                    break



solution(T)
    # answer = result
    # return answer