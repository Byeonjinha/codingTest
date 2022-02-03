import sys
from itertools import combinations
n = int(sys.stdin.readline())
sorted_location = []
for _ in range(n):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    sorted_location.append((x, y, z))
dic = {}
ss = list(combinations(list(set(sorted_location)),2))
for i in range(len(ss)):
    if  (ss[i][0][0]-ss[i][1][0])**2 + (ss[i][0][1]-ss[i][1][1])**2 + (ss[i][0][2]-ss[i][1][2])**2  not  in dic :
        print(ss[i], (ss[i][0][0]-ss[i][1][0])**2 + (ss[i][0][1]-ss[i][1][1])**2 + (ss[i][0][2]-ss[i][1][2])**2  )
        dic[ (ss[i][0][0]-ss[i][1][0])**2 + (ss[i][0][1]-ss[i][1][1])**2 + (ss[i][0][2]-ss[i][1][2])**2     ] = 1
    else:
        print(ss[i],
              (ss[i][0][0] - ss[i][1][0]) ** 2 + (ss[i][0][1] - ss[i][1][1]) ** 2 + (ss[i][0][2] - ss[i][1][2]) ** 2)
        dic[(ss[i][0][0] - ss[i][1][0]) ** 2 + (ss[i][0][1] - ss[i][1][1]) ** 2 + (ss[i][0][2] - ss[i][1][2]) ** 2 ] += 1
print(min(dic))
print(dic.get(min(dic)))