def find_min_difference(N, ingredients):
    min_difference = float('inf')  # 무한대로 초기화

    # 모든 재료의 조합을 확인하기 위한 반복문
    for i in range(1, N + 1):
        for combination in itertools.combinations(ingredients, i):
            s_sum, b_sum = 1, 0  # 요리의 신맛과 쓴맛 초기값 설정

            # 각 조합에 대한 신맛과 쓴맛 계산
            for s, b in combination:
                s_sum *= s
                b_sum += b

            # 차이가 최소인 경우 갱신
            min_difference = min(min_difference, abs(s_sum - b_sum))

    return min_difference

import itertools

# 입력 처리
N = int(input())
ingredients = []
for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))

# 결과 출력
print(find_min_difference(N, ingredients))