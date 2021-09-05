N = int(input())
Grade = []

c=list(map(int,input().split()))


Grade2=[]
MGrade = max(c)
Sumgrade=int(0)

for A in range(0,N):

    NGrade = c[A] / int(MGrade)*100
    Grade2.append(NGrade)
    Sumgrade=Sumgrade+NGrade
X= Sumgrade/len(Grade2)
print(X)

