def solution(myString, pat):
    return myString[:len(myString) - ''.join(list(reversed(myString))).index(''.join(list(reversed(pat))))]