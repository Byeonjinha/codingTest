from itertools import combinations
a= []
for i in range(9):
    n=int(input())
    a.append(n)

b=  list(combinations(a,7))
for i in b:
    if sum(i) == 100:
       answer = sorted(list(i))
for i in answer:
    print(i)
