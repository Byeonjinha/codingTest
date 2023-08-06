import math
from itertools import combinations

ingredients_count = int(input())
ingredients = [list(map(int, input().split())) for _ in range(ingredients_count)]
answer = math.inf
for i in range(1, ingredients_count + 1):
    for j in combinations(ingredients, i):
        S = 1
        B = 0
        for k in j:
            S *= k[0]
            B += k[1]
        answer = min(abs(S - B), answer)
print(answer)