import sys
from itertools import product
from itertools import permutations
from itertools import combinations
N,M = map(int, sys.stdin.readline().split())


def min(M):
    card = map(int,sys.stdin.readline().split())
    cardsumlist = list(combinations(card,3))
    cardsumlist2=[]
    for xx in range(0,len(cardsumlist)):
        cardsumlist2.append(sum(cardsumlist[xx]))
    cardsumlist2.sort()
    i = int(0)
    while True:
        if M <= cardsumlist2[i] or cardsumlist2[i]==cardsumlist2[-1] :
            break
        i+=1
    if cardsumlist2[i]==M:
        print(cardsumlist2[i])
    elif cardsumlist2[i]>M:
        print(cardsumlist2[i-1])
    else:
        print(cardsumlist2[i])
min(M)