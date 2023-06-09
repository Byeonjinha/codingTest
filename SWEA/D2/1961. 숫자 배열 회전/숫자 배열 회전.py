# 테스트 케이스의 개수 T를 입력받음
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(1, T + 1):
    # N을 입력받음
    N = int(input())

    # N x N 행렬을 입력받음
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전한 결과를 저장할 2차원 배열 생성
    rotated_90 = [[0] * N for _ in range(N)]

    # 180도 회전한 결과를 저장할 2차원 배열 생성
    rotated_180 = [[0] * N for _ in range(N)]

    # 270도 회전한 결과를 저장할 2차원 배열 생성
    rotated_270 = [[0] * N for _ in range(N)]

    # 주어진 행렬을 회전하여 결과를 저장

    for i in range(N):
        for j in range(N):
            # 90도 회전
            rotated_90[j][N - i - 1] = matrix[i][j]
            # 180도 회전
            rotated_180[N - i - 1][N - j - 1] = matrix[i][j]
            # 270도 회전
            rotated_270[N - j - 1][i] = matrix[i][j]
    answer = []

    for y in range(N):
        piece = ""
        for x in range(N):
            piece += str(rotated_90[y][x])
        piece += " "
        for x in range(N):
            piece += str(rotated_180[y][x])
        piece += " "
        for x in range(N):
            piece += str(rotated_270[y][x])
        piece += " "
        answer.append(piece)
    # 회전한 결과 출력
    print("#{}".format(t))
    for i in answer:
        print(i)

