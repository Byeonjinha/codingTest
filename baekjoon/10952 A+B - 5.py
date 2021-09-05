x=int()
y=int()
while True :
    x, y = input().split()
    x=int(x)
    y=int(y)
    if x==0 and y==0:
        break
    else :
        x=int(x)
        y=int(y)

        print(x+y)