def find_min_removal_count(n, wires):
    # 전깃줄을 B 위치를 기준으로 오름차순 정렬
    wires.sort(key=lambda x: x[1])

    # LIS (가장 긴 증가하는 부분 수열)을 찾는 함수
    def find_lis(arr):
        lis = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i][0] > arr[j][0]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)

    # 가장 긴 증가하는 부분 수열의 길이를 전체 전깃줄 개수에서 빼면 최소 제거해야 하는 개수를 얻을 수 있음
    lis_length = find_lis(wires)
    min_removal_count = n - lis_length

    return min_removal_count

# 입력 처리
n = int(input())  # 전깃줄의 개수
wires = []  # 전깃줄의 위치 정보를 저장할 리스트

for _ in range(n):
    a, b = map(int, input().split())  # A와 B의 위치 정보 입력
    wires.append((a, b))

# 최소 제거해야 하는 전깃줄 개수 구하기
result = find_min_removal_count(n, wires)
print(result) 