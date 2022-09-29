import sys
from collections import defaultdict
dices = sys.stdin.readline().split()
dicesValue = defaultdict(int)
answer = 0

for i in dices:
    dicesValue[i] += 1

invertDic = {v:k for k,v in dicesValue.items()}
if max(dicesValue.values()) == 3:
    answer += 10000 + int(invertDic[3])* 1000
elif max(dicesValue.values()) == 2:
    answer += 1000 + int(invertDic[2])* 100
else:
    answer = int(max(dicesValue))*100
print(answer)
