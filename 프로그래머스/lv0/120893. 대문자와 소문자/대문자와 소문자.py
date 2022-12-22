from string import ascii_lowercase
from string import ascii_uppercase
def solution(my_string):
    lower = list(ascii_lowercase)
    upper = list(ascii_uppercase)
    answer = ""
    for i in my_string:
        if i in lower :
            answer += upper[lower.index(i)]
        else :
            answer += lower[upper.index(i)]
    return answer