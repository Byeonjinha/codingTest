from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


# from collections import  deque
# import sys
# sys.setrecursionlimit(10**6)
# answer=[]
# def stockprice(prices):
#     leftnum = prices.popleft()  #  prices 에서 하나뺌
#
#     if leftnum > min(prices):
#         for i in prices:
#             if leftnum> i:                         #더작은수가 있으면 비교하고 넣음
#                 answer.append(prices.index(i)+1)
#                 break
#     else:
#         answer.append(len(prices))                # 더작은수가 없으면 걍넣음
#
#
#     if len(prices)==1:
#         answer.append(0)
#         return                                      #prices 의 크기가 1이면 0추가하고 종료
#     else:
#         stockprice(prices)                          #재귀
#
# def solution(prices):
#     prices=deque(prices)                             #prices 데크로만듬
#     stockprice(prices)                              #재귀식실행
#     print(answer)
#     return answer
#
prices = [1, 2, 3, 2, 3,1, 2, 3, 2, 3,1, 2, 3, 2, 3]
solution(prices)