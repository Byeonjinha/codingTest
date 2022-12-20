def solution(my_string, n):
    my_string = [i*n for i in my_string]
    return ''.join(my_string)