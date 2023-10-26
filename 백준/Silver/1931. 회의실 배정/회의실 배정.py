import math

n = int(input())

schedule = []

for _ in range(n):
    start, end = map(int, input().split())
    schedule.append([start, end])

schedule.sort(key = lambda x: (x[1], x[0]))

answer = 0
last_end = 0

for start, end in schedule:
    if start >= last_end:
        answer += 1
        last_end = end

print(answer)

