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
print({1,2,3,4}.isdisjoint({3,4,5,6}))
print({1,2,3,4}.isdisjoint({7,8,9}))
# issubset() - 부분집합(subset)인가?
print({3,4}.issubset({2,3,4,5}))
print({1,4,7}.issubset({2,3,4,5}))
# issuperset() - 확대집합(superset)인가?
print({2,3,4,5}.issuperset({3,4}))
print({2,3,4,5}.issuperset({1,4,7}))

# union() - 합집합을 만들어 리턴
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
# update() - 합집합을 만들어 원본 데이터를 갱신(수정)
s1.update(s2)
print(s1)
# difference() - 차집합을 만들어 리턴
s1={1,2,3,4,5}
print(s1.difference(s2))
# difference_update() - 차집합을 만들어 원본 데이터를 갱신
s1.difference_update(s2)
print(s1)

# intersection() - 교집합을 만들어 리턴
s1={1,2,3,4,5}
print(s1.intersection(s2))
# intersection_update() - 교집합을 만들어 원본 데이터를 갱신
s1.intersection_update(s2)
print(s1)
# symmetric_difference() - 대칭차를 만들어 리턴
s1 ={1,2,3,4,5}
print(s1.symmetric_difference(s2))

# symmetric_difference_update() - 대칭차를 만들어 원본 데이터를 갱신
s1.symmetric_difference_update(s2)
print(s1)