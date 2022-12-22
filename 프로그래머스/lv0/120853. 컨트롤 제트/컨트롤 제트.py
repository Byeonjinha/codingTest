def solution(s):
    numArray = []
    for i in s.split():
        if i == "Z" :
            numArray.pop()
        else :   
            numArray.append(int(i))
    return sum(numArray)