def solution(my_string, alp):
    my_string = list(my_string)
    while alp in my_string:
        my_string[my_string.index(alp)] = alp.upper()
    return ''.join(my_string)