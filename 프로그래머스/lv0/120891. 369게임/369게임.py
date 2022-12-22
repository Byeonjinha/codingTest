from collections import Counter
def solution(order):
    orderArray = Counter(str(order))
    answer = orderArray['3'] + orderArray['6'] + orderArray['9'] 
    return answer