def solution(arr):
    b = []
    dic ={}
    for i in range(len(arr)):
        count = 1
        a = []
        while arr[i]!=1:
            count+=1
            if arr[i]%count==0:
                arr[i] /= count
                a.append(count)
                count =1
        b.append(a)
    for j in range(len(b)):
        for j2 in range(len(b[j])):
            if b[j][j2] not in dic:
                dic[b[j][j2]] =  b[j].count(b[j][j2])
            elif dic[b[j][j2]] < b[j].count(b[j][j2]):
                dic[b[j][j2]] = b[j].count(b[j][j2])
    answer = 1
    for k in dic:
        answer *= k**(dic.get(k))

    return answer

arr=  [1,2,3]
solution(arr)