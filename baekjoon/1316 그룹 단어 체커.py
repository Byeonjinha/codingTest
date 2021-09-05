N= int(input())
temp=str("KING")
swn=[]
swn2=[]
testswn2=[]
n=int(0)
for A in range(0,N):
    AAA= input()
    for B in AAA:
        if B!=temp:
            swn2.append(B)
        temp=B
    temp=str("KING")
    testswn2=list(set(swn2))
    if len(swn2)==len(testswn2):
        n+=1
    swn2.clear()
print(n)
