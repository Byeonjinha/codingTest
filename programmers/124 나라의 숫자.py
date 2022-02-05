from itertools import product
def solution(word):
    a= []
    for i in range(1, 6):
        a+= list(map(''.join,product(['A', 'E', 'I', 'O', 'U'], repeat=i)))
    a.sort()
    return a.index(word) + 1
word="A"
solution(word)