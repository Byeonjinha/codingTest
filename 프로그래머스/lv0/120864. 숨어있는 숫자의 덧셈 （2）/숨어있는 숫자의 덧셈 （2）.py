def solution(my_string):
    answer = 0
    num = "0"
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            num += my_string[i]
        else :
            answer += int(num)
            num = "0"
    answer += int(num)
    return answer