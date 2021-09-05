N=int(input())
temp=int()
sum=int()
for A in range(0,N):
    L=input()
    for B in L:
        if B=="O":
            temp+=1
        elif B=="X":
            temp=0
        sum+=temp
    print(sum)
    sum=0
    temp=0
