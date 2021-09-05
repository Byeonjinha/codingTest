# answer=0
# def dfs(numbers,target,sum,idx):
#     global answer
#     if target == sum and idx==len(numbers):
#         answer+=1
#         return
#     if target != sum and idx==len(numbers):
#         return
#     else:
#         dfs(numbers,target,sum+numbers[idx],idx+1)
#         dfs(numbers,target,sum-numbers[idx],idx+1)
# def solution(numbers, target):
#     global answer
#     dfs(numbers,target,0,0)
#     return answer
from collections import deque
answer = 0
def bfs(numbers,target,sum,idx):
    global answer
    queue = deque([(sum,idx)])
    while queue:
        sum ,idx = queue.popleft()
        if sum == target and idx==len(numbers):
            answer+=1

        elif sum != target and idx==len(numbers):
            pass
        else:
            queue.append([sum+numbers[idx],idx+1])
            queue.append([sum-numbers[idx],idx+1])
    return

def solution(numbers, target):
    global answer

    bfs(numbers,target,0,0)
    print(answer)
    return answer


numbers = [1, 1, 1, 1, 1]
target  = 3
solution(numbers, target)