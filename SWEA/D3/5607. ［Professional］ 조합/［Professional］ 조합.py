def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % 1234567891
    return result

# 테스트 케이스의 개수 입력
T = int(input())

for tc in range(1, T + 1):
    # 자연수 N과 R 입력
    N, R = map(int, input().split())

    # N combination R 계산
    numerator = factorial(N)
    denominator = (factorial(R) * factorial(N - R)) % 1234567891
    result = (numerator * pow(denominator, 1234567889, 1234567891)) % 1234567891

    # 결과 출력
    print("#{} {}".format(tc, result))
