def solution(s):
    stack=[]
    for i in range(0,len(s)):
        print(stack)
        if len(stack) != 0 and s[i] ==stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack)==0:
        return 1
    return 0
s= "baabaa"
solution(s)