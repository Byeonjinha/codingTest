# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    # N 값 입력
    N = int(input())

    # 파스칼의 삼각형 초기화
    triangle = [[0] * N for _ in range(N)]

    # 파스칼의 삼각형 생성
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    # 결과 출력
    print("#{}".format(test_case))
    for row in triangle:
        for num in row:
            if num != 0:
                print(num, end=" ")
        print()
