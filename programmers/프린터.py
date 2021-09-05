from collections import deque
def solution(priorities, location):
    queue2 = deque([0 for _ in range(len(priorities))])
    queue = deque(priorities)
    queue2[location]=1
    count=0
    while sum(queue2)!=0:
        if queue[0]==max(queue):
            queue.popleft()
            queue2.popleft()
            count+=1
        else:
            v=queue.popleft()
            v2=queue2.popleft()
            queue.append(v)
            queue2.append(v2)
    return count

    # return answer



priorities= [2, 1, 3, 2]
location =2

solution(priorities, location)