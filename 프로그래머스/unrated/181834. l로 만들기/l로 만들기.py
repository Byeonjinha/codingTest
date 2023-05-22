from string import ascii_lowercase
alpha = list(ascii_lowercase) 
def solution(myString):
    answer = ''
    for i in myString:
        if alpha.index(i) > alpha.index("l"):
            answer += i
        else:
            answer += "l"
    return answer