from collections import defaultdict

def solution(array, n):
    dictionary = defaultdict(int)
    for i in array:
        dictionary[i] += 1
    if n in dictionary:    
        return dictionary[n]
    return 0