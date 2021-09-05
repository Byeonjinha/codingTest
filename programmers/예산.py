def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        budget -= d[i]
        if budget==0:
            return i+1
        elif budget <0:
            return i
    return(i+1)




d = [1,3,2,5,4]
budget =100
solution(d, budget)