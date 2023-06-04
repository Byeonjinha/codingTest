from collections import Counter

T = int(input())
for tc_idx in range(T):
    winlose = Counter(input())
    if winlose["x"] >= 8: print("#"+str(tc_idx + 1), "NO");
    else: print("#"+str(tc_idx + 1), "YES")