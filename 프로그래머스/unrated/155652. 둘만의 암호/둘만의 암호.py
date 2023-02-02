from string import ascii_lowercase
def solution(s, skip, index):
    newAlpha = set(ascii_lowercase) - set(list(skip))
    newAlpha = sorted(newAlpha)
    answer = ''
    for i in range(len(s)):
        newIdx = newAlpha.index(s[i]) + index
        answer += newAlpha[newIdx % len(newAlpha)]
    return answer