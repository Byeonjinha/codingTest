import collections

s=['a','b','c','d','a','b','c']
s2=['a','b','c','d','a','b']
d={}
for k in s:
    d.setdefault(k,0)
    d[k]+=1
# print(list(d.items()))

d=collections.defaultdict(int)
for k in s:
    d[k]+=1
    print(d)
print(dict(d))
p=collections.Counter(s)
p2=collections.Counter(s2)
print(p-p2)
