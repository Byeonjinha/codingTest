T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 압축된 문서의 알파벳과 숫자 쌍의 개수

    uncompressed = ''  # 원본 문서를 저장할 변수

    for _ in range(N):
        alpha, count = input().split()  # 알파벳과 알파벳의 연속된 개수를 입력받음
        count = int(count)  # 연속된 개수를 정수로 변환

        uncompressed += alpha * count  # 알파벳을 연속된 개수만큼 반복하여 원본 문서에 추가

    # 원본 문서를 10개씩 잘라 출력
    print(f"#{tc}")
    for i in range(0, len(uncompressed), 10):
        print(uncompressed[i:i+10])
