def solution(num_list):
    multiply = 1
    for i in num_list:
        multiply *= i
    if multiply < pow(sum(num_list) , 2): return 1
    return 0