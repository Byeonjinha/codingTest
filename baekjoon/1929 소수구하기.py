import sys

N ,M = map(int,sys.stdin.readline().split())
asdf=int(0)
if N ==1:
    N=2
sosulist =[]
count = int(0)
for x in range(N,M+1):
    for ii in range(0,len(sosulist)):
        if x%sosulist[ii]==0:
            asdf+=1
            break   
    if asdf>0:
        asdf-=1
        continue

    for x2 in range(2, int(x**0.5)+1):
        if x%x2 == 0 :
            count+=1
    if count ==0 :
        sosulist.append(x)
    count=0
if len(sosulist)==0:
    print("-1")
else:
    for x in range(0,len(sosulist)):
        print(sosulist[x])
'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

'''
