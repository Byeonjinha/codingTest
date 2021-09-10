s= {-7,0,-5,14,1,2,3,4,5,6,7}
type(s)
print(s)
print(len(s))
print(5 in s)
print(8 in s)
print(s - {5,6,7,8,9})
print(s&{5,6,7,8,9})
print(s|{5,6,7,8,9})
print(s=={5,6,7,8,9})
s.add(10)
print(s)
s.remove(10)
print(s)
s.discard(4)
print(s)
print(s.pop())
print(s)
ss = s.copy()
print(ss,"ss")
ss.clear()
print(ss,"ss")

# isdisjoint() - 두 집합이 공통 원소를 갖지 않는가?
#
# issubset() - 부분집합(subset)인가?
#
# issuperset() - 확대집합(superset)인가?