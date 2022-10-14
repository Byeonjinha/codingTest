totalScore = 0
for _ in range(5):
    A = int(input())
    if A <= 40:
        totalScore += 40
    else:
        totalScore += A
print(totalScore//5)