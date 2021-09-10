import sys

n= int(sys.stdin.readline())
for k in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    R =[r1,r2,r]
    m=max(R); R.remove(m)
    print(-1 if(r==0 and r1==r2) else 1 if (r == r1+r2 or m==sum(R)) else 0 if(m>sum(R)) else 2)