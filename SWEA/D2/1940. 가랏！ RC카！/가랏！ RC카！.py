T = int(input())

for tc in range(1, T+1):
    N = int(input())  # command의 수

    speed = 0  # 초기 속도
    distance = 0  # 이동 거리

    for _ in range(N):
        command = list(map(int, input().split()))

        if command[0] == 0:  # 현재 속도 유지
            distance += speed
        elif command[0] == 1:  # 가속
            speed += command[1]
            distance += speed
        elif command[0] == 2:  # 감속
            speed -= command[1]
            if speed < 0:  # 속도가 음수일 경우, 0으로 조정
                speed = 0
            distance += speed

    print(f"#{tc} {distance}")
