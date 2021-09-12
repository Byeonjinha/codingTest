def solution(v):
    l = v
    x = 0
    y = 0
    p = (list(zip(l[0], l[1], l[2])))

    if p[0].count(p[0][0]) == 1:
        x = p[0][0]
    elif p[0].count(p[0][1]) == 1:
        x = p[0][1]
    else:
        x = p[0][2]

    if p[1].count(p[1][0]) == 1:
        y = p[1][0]
    elif p[1].count(p[1][1]) == 1:
        y = p[1][1]
    else:
        y = p[1][2]

    return [x, y]

v= [[1, 4], [3, 4], [3, 10]]
solution(v)