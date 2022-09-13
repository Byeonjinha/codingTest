import sys

input = sys.stdin.readline
n = int(input())
pl = [tuple(map(int, input().split())) for i in range(n)]
pl = list(set(pl))
dic = {}
key = {}
# x축 기준 정렬
pl.sort()


# 두 점 사이의 거리 계산 함수
def getDist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
#
def Sort1(t, target_pl, minDist):
    for i in range(t - 1):
        for j in range(i + 1, t):
            if (target_pl[i][1] - target_pl[j][1]) ** 2+(target_pl[i][2] - target_pl[j][2]) ** 2 <= minDist:
                minDist = min(minDist, getDist(target_pl[i], target_pl[j]))
                if minDist == getDist(target_pl[i], target_pl[j]) and (target_pl[i], target_pl[j]) not in key and (target_pl[j], target_pl[i]) not in key:
                    key[(target_pl[i], target_pl[j])] = 0

                    if minDist not in dic:
                        dic[minDist] = 1
                    else:
                        dic[minDist] += 1
            else:
                break
                # 현재 후보 점이 다음 점과 최소 거리보다 멀다면 더 볼 필요가 없음.
                # 위 처리가 없으면 시간 초과 발생


def dac(start, end):
    # 점이 두 개 남으면 사이의 거리 리턴
    if end - start == 1:
        return getDist(pl[start], pl[end])

    # 분할정복 실행
    mid = (start + end) // 2
    minDist = min(dac(start, mid), dac(mid, end))

    # x축 기준으로 후보 점들을 찾는다.
    target_pl = []
    for i in range(start, end + 1):
        if (pl[mid][0] - pl[i][0]) ** 2 <= minDist:
            target_pl.append(pl[i])

    t = len(target_pl)
    # y축 기준 정렬
    target_pl.sort(key=lambda x: (x[1]))
    Sort1(t, target_pl, minDist)

    target_pl.sort(key=lambda x: (x[2]))
    Sort1(t, target_pl, minDist)

    return minDist


dac(0, len(pl) - 1)
print(min(dic))

print(dic.get(min(dic)))