from string import ascii_lowercase
def solution(age):
    answer = ''
    lower = list(ascii_lowercase)[:10]
    for i in str(age):
        answer += lower[int(i)]
    return answer