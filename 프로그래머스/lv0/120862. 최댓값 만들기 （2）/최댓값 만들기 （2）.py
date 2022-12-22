from itertools import combinations
def solution(numbers):
    maxNum = -999999999999
    for x,y in combinations(numbers,2):
        maxNum = max(maxNum, x*y)
    return maxNum