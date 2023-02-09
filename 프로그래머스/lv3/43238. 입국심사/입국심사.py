def solution(n, times):
    answer = 0
    최소값, 최대값 = 1, max(times) * n
    while 최소값 <= 최대값:
        중앙값 = (최소값 + 최대값) // 2
        검색받은사람 = 0
        for time in times:
            검색받은사람 += 중앙값 // time
            if 검색받은사람 >= n:
                break
        if 검색받은사람 >= n:
            answer = 중앙값
            최대값 = 중앙값 - 1
        elif 검색받은사람 < n:
            최소값 = 중앙값 + 1
    return answer