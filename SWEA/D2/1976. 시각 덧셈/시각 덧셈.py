# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    # 시 분 값 입력
    h1, m1, h2, m2 = map(int, input().split())

    # 시 분을 분 단위로 변환
    time1 = h1 * 60 + m1
    time2 = h2 * 60 + m2

    # 시간 덧셈
    total_minutes = time1 + time2

    # 시 분으로 변환
    hours = total_minutes // 60
    minutes = total_minutes % 60

    # 12시간제로 표시하기 위해 시간 조정
    if hours > 12:
        hours -= 12

    # 결과 출력
    print("#{} {} {}".format(test_case, hours, minutes))
