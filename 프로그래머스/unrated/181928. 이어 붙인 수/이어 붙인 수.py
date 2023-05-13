def solution(num_list):
    odd = "0"
    even = "0"
    for num in num_list:
        if num % 2 == 0:
            odd += str(num)
        else:
            even += str(num)
    return int(odd) + int(even)