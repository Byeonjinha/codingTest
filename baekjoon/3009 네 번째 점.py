import sys
l=[]
x=0
y=0
for i in range(3):
    l.append(list(map(int,sys.stdin.readline().split())))
p=(list(zip(l[0],l[1],l[2])))

if p[0].count(p[0][0])==1:
   x=p[0][0]
elif p[0].count(p[0][1])==1:
    x=p[0][1]
else:
    x=p[0][2]

if p[1].count(p[1][0])==1:
   y=p[1][0]
elif p[1].count(p[1][1])==1:
    y=p[1][1]
else:
    y=p[1][2]
print(x,y)