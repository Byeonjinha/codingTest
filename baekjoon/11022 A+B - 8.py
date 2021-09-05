a = int(input())
b = []
for n2 in range(1,a+1):
    c = map(int, input().split())
    c=list(c)
    b.append(c)
m=int(0)
while a>m:
    list = b
    d=list[m]
    e=d[0]
    f=d[1]
    print(f"Case #{m+1}:", e,"+",f,"=",sum(list[m]))
    m+=1
