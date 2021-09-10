import sys
def Fsosu(N):
    count = int(0)
    sosu=[]
    for a in range(2,N):
        for b in range(2,a):
            if a%b ==0:
                count+=1
        if count==0:
            sosu.append(a)
        count=0
                  #소수만드는기능
    return sosu
def Fcountsosu(N):
    M= sys.stdin.readline().split()
    n=(0)
    sosulist=Fsosu(1000)
    for i in M:
        if sosulist.count(int(i)) > 0:
            n=n+1
    return n

N= sys.stdin.readline()

print(Fcountsosu(N))
