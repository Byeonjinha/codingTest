import sys
N=int(sys.stdin.readline())
if N==0:
    print(0)
else:
    count=0
    suuzza='666'

    while count!=N:
        if '666' in suuzza :
            count+=1
        suuzza=str(int(suuzza)+1)
    print(int(suuzza)-1)