#bfs 풀이
# import collections
#
# def solution(numbers, target):
#     answer = 0
#     stack = collections.deque([(0, 0)])
#     while stack:
#         print(stack , " queue")
#         current_sum, num_idx = stack.popleft()
#         print(current_sum,num_idx)
#
#         if num_idx == len(numbers):
#             if current_sum == target:
#                 answer += 1
#         else:
#             number = numbers[num_idx]
#             stack.append((current_sum+number, num_idx + 1))
#             stack.append((current_sum-number, num_idx + 1))
#     return answer
#
# numbers= [1, 1, 1, 1, 1]
# target =3
# solution(numbers, target)

# dfs 풀이
# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return
#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
#
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer