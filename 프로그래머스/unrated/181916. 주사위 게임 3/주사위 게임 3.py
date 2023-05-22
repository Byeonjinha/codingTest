from collections import Counter
def solution(a, b, c, d):
    answer = 0
    cc = Counter([a, b, c, d])
    if len(cc) == 1:
        for i in cc:
            answer += i * 1111
    elif len(cc) == 3:
        point = 1
        for i in cc:
            if cc[i] == 1:
                point *= i
        answer += point
    elif len(cc) ==2:
        point = 0
        a = []
        b = []
        for i in cc:
            if cc[i] == 2:
                a.append(i)
            elif cc[i] == 3:
                b.insert(0, i)
            else:
                b.append(i)
        if len(a) != 0:
            point = (a[0] + a[1]) * abs(a[0] - a[1])
        else:
            point = (10 * b[0] + b[1]) ** 2
        answer += point
    elif len(cc) == 4:
        answer += min(a, b, c, d)
    return answer