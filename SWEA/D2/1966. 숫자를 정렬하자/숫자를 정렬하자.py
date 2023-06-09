# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(1, T + 1):
    # N을 입력받음
    N = int(input())

    # N 길이의 숫자열을 입력받음
    numbers = list(map(int, input().split()))

    # 숫자열을 오름차순으로 정렬
    sorted_numbers = sorted(numbers)

    # 정렬된 결과 출력
    print("#{} {}".format(t, " ".join(map(str, sorted_numbers))))
