from collections import Counter
N = int(input())
for i in range(1, N + 1):
    count = 0 
    if "3" in list(str(i)) or "6" in list(str(i)) or "9" in list(str(i)):
        for j in Counter(list(str(i))):
            if j == "3" or j == "6" or j =="9":
                count += Counter(list(str(i)))[j]
        print("-" * count , end = " ")
    else:
        print(i, end = " ")