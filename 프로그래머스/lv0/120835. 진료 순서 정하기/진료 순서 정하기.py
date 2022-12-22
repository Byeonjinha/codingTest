def solution(emergency): 
    answer = []
    newArray = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(newArray.index(i)+1)
    return answer