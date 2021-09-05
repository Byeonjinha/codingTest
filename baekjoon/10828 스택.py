import sys
stack=[]

N = int(sys.stdin.readline())

def solution(N):
    commend = ""
    for i in range(N):
        commend = sys.stdin.readline().split()
        if len(commend)>1:
            push(commend)
        elif len(commend)==1:
            if commend[0] == "top":
                top(commend)
            if commend[0] == "pop":
                pop(commend)
            if commend[0] == "size":
                size(commend)
            if commend[0] == "empty":
                empty(commend)
def pop(commend):
    if len(stack) == 0:
        print("-1")
    elif len(stack) == 1:
        print(stack[0])
        stack.pop(0)
    else:
        print(stack[-1])
        stack.pop(-1)
def top(commend):
    if len(stack) == 0:
        print("-1")
    elif len(stack) == 1:
        print(stack[0])
    else:
        print(stack[-1])
def push(commend):
    stack.append(commend[1])

def size(commend):
    print(len(stack))

def empty(commend):
    if len(stack) ==0:
        print("1")
    else :
        print("0")

solution(N)