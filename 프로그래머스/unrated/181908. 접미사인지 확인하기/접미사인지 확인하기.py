def solution(my_string, is_suffix):
    h = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in h:
        return 1
    return 0