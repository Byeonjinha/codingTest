def solution(lines):
    answer = 0
    total = []
    lines1 = [i for i in range(lines[0][0],lines[0][1])]
    lines2 = [i for i in range(lines[1][0],lines[1][1])]
    lines3 = [i for i in range(lines[2][0],lines[2][1])]
    for i in lines1:
        if i in lines2 and i not in total:
            answer += 1
            total.append(i)
    for i in lines1:
        if i in lines3 and i not in total:
            answer += 1
            total.append(i)
    for i in lines2:
        if i in lines3 and i not in total:
            answer += 1
            total.append(i)
    return answer