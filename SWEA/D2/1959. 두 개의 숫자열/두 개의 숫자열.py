# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(1, T + 1):
    # N과 M을 입력받음
    N, M = map(int, input().split())

    # Ai와 Bj를 입력받음
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 더 긴 숫자열과 짧은 숫자열을 결정
    if N > M:
        long_arr, short_arr = Ai, Bj
    else:
        long_arr, short_arr = Bj, Ai

    max_sum = 0  # 최댓값 초기화

    # 가능한 모든 숫자 위치 조합 확인
    for i in range(len(long_arr) - len(short_arr) + 1):
        temp_sum = 0  # 현재 조합에서의 곱의 합

        # 숫자 위치 변경하여 곱의 합 계산
        for j in range(len(short_arr)):
            temp_sum += long_arr[i + j] * short_arr[j]

        # 현재 조합의 곱의 합이 최댓값보다 크면 최댓값 갱신
        if temp_sum > max_sum:
            max_sum = temp_sum

    # 최댓값 출력
    print("#{} {}".format(t, max_sum))
