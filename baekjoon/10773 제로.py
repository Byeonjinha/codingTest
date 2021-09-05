import sys
donlist=[]
def solution(K):
    for i in range(K):
        jungsoo=int(sys.stdin.readline())
        if jungsoo !=0:
            don(jungsoo)
        else:
            jium(jungsoo)
    if len(donlist)==0:
        print("0")
    else :
        print(sum(donlist))
def don(jungsoo):
    donlist.append(jungsoo)
def jium(jungsoo):
    donlist.pop(-1)

K=int(sys.stdin.readline())
solution(K)