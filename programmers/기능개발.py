def solution(progresses, speeds):
    answer=[]
    ok = [0 for _ in range(len(progresses))]
    while len(ok)!=0:

        for i in range(0,len(progresses)):
            progresses[i]+=speeds[i]
            if progresses[i]>=100:
                ok[i]=1
        count = 0
        for i in range(len(ok)):

            if ok[0]==1:
                ok.remove(ok[0])
                progresses.remove(progresses[0])
                speeds.remove(speeds[0])
                count+=1
        if count !=0:
            answer.append(count)

    return answer

progresses= [0,0,0,0]
speeds=[100,50,34,25]

solution(progresses, speeds)