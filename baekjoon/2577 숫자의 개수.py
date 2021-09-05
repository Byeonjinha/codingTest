x=[]
y=[]
for A in range(0,9):
    a = int(input())
    x.append(a)
    y.append(A)
print(max(x))
for A in range(0,9):
    if x[A]==max(x):
        print(int(A)+1)
