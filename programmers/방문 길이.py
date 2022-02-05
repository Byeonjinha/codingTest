key = []
def solution(dirs):
    map = [[False for _ in range(11)] for _ in range(11)]

    map[5][5] = True
    current1=[5,5]
    current2=[5,5]
    count = 0

    for i in range(len(dirs)):
        if dirs[i] == "U":
            current1[1]+=1
            if current1[1]>10:
                current1[1]=10
                continue
        elif dirs[i] == "D":
            current1[1]-=1
            if current1[1]<0:
                current1[1]=0
                continue
        elif dirs[i] == "L":
            current1[0]-=1
            if current1[0]<0:
                current1[0]=0
                continue
        elif dirs[i] == "R":
            current1[0]+=1
            if current1[0]>10:
                current1[0]=10
                continue
        print(current1,current2,key)
        if [current1,current2] in key or [current2,current1] in key :
            current2=current1.copy()
        else:
            key.append([current2.copy(),current1.copy()])
            count+=1
            current2=current1.copy()
    answer = count

    return answer


dirs="LRLRL"

solution(dirs)