from collections import Counter
from collections import defaultdict
def solution(topping):
    answer = 0
    toppingA = Counter(topping)
    toppingB = defaultdict(int)
    for i in topping:
        toppingA[i] -= 1
        if toppingA[i] == 0:
            toppingA.pop(i)
        toppingB[i] += 1
        if len(toppingA) == len(toppingB) :
            answer += 1
    return answer