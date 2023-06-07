# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    # 입력 값 받기
    P, Q, R, S, W = map(int, input().split())

    # A사 요금 계산
    cost_A = P * W

    # B사 요금 계산
    if W <= R:
        cost_B = Q
    else:
        cost_B = Q + (W - R) * S

    # 더 저렴한 요금 출력
    if cost_A < cost_B:
        print("#{} {}".format(test_case, cost_A))
    else:
        print("#{} {}".format(test_case, cost_B))
