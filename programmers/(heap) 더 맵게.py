import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        print(scoville)
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    print(answer)
    return answer


scoville=[1, 2, 3, 9, 10, 12]
K=	7

solution(scoville, K)