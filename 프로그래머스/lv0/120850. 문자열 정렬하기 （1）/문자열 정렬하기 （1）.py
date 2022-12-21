def solution(my_string):
    answer = []
    my_array = sorted(list(my_string))
    for i in my_array:
        if i.isdigit() :
            answer.append(int(i))
    return answer