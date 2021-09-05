N = int(input())

C = int(N)
N2 =int(0)
TEMP1=str()
TEMP2=int()
SUM= int(0)
N=str(N)
SUM2= int(0)
count1 = int(0)

if int(N) == 0:
    count1+=1
while C!=SUM2:
    N=str(N)
    SUM = int(0)
    SUM2=str(SUM2)
    for TEMP1 in N:
        TEMP1=str(TEMP1)
    for TEMP2 in N:
        TEMP2=int(TEMP2)
        SUM=int(SUM)
        SUM=SUM+TEMP2
        SUM= str(SUM)
        for X2 in SUM:
            SUM=X2
    TEMP1=str(TEMP1)
    SUM2 = TEMP1+SUM
    N=int(SUM2)
    SUM2=int(SUM2)
    count1+=1
print(count1)
