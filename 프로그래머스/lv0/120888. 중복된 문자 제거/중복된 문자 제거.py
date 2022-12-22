def solution(my_string):
    answer = ''
    isIn = []
    for i in my_string:
        if i not in isIn :
            isIn.append(i)
            answer += i
    return answer