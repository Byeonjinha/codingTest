from collections import  deque
import sys
queue=deque()
def push(M):
    queue.append(M[1])
def pop(M):
    if len(queue)<1:
        print(-1)
    else:
        v=queue.popleft()
        print(v)
def size(M):
    print(len(queue))
def empty(M):
    if len(queue)<1:
        print(1)
    else:
        print(0)
def front(M):
    if len(queue)<1:
        print(-1)
    else:
        print(queue[0])
def back(M):
    if len(queue)<1:
        print(-1)
    elif len(queue)==1:
        print(queue[0])
    else:
        print(queue[-1])

N= int(sys.stdin.readline())
for i in range(N):
    M= sys.stdin.readline().split()
    if M[0]=='push':
        push(M)
    if M[0]=='pop':
        pop(M)
    if M[0]=='size':
        size(M)
    if M[0]=='empty':
        empty(M)
    if M[0]=='front':
        front(M)
    if M[0]=='back':
        back(M)

