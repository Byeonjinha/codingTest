from string import ascii_uppercase

A=list(ascii_uppercase)
B=list( 0 for i in range(26) )
n=int(3)
for x in range(0,19):
    B[x]=B[x]+n
    if (x+1)%3==0:
        n+=1
B[18]=B[18]-1
n=int(9)
for x in range(19,25):
    B[x]=B[x]+n
    if (x)%3==0:
        n+=1
B[25]=10
text = input()
result = int(0)
for i in text:
    for j in A:
        if i==j:
            result= result+B[(A.index(j))]
print(result)