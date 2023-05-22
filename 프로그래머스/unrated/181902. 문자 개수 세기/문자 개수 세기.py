from string import ascii_lowercase, ascii_uppercase

def solution(my_string):
    alpha = {i: 0 for i in ascii_uppercase + ascii_lowercase }
    for i in my_string:
        alpha[i] += 1
    answer = []
    for i in alpha:
        answer.append(alpha[i])
    return answer