def solution(arr1, arr2):
    arr2_2 = list(map(list, zip(*arr2)))
    answer = []
    for i in range(len(arr1)):
        a = []
        for j in range(len(arr2_2)):
            b = 0
            for i2 in range(len(arr1[i])):
                b= b+ arr1[i][i2]*arr2_2[j][i2]
            a.append(b)
        answer.append(a)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
arr2_2 = [[5, 2, 3], [4, 4, 1], [3, 1, 1]]
solution(arr1, arr2)