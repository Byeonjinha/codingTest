import sys
n = sys.stdin.readline().strip().split("-")
answer = ""
for i in n:
    answer += i[0]
print(answer)