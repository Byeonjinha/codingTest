def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for member in photo:
        point = 0
        for j in member:
            try:
                point += dic[j]
            except:
                continue
        answer.append(point)
    return answer