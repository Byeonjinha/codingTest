from itertools import  combinations

people	=[70, 50, 80, 50]
limit	= 100
def solution(people, limit):
    people.sort()
    count=0
    i=0
    print(people)
    while True:
        if people[i]+people[i+1]<=limit:
            people.remove(people[0])
            people.remove(people[0])
            count+=1
            if len(people) <2:
                break
        else:
            people.remove(people[0])
            count+=1
            if len(people) < 2: break
    return(count+1)
    print(count+1)
solution(people, limit)