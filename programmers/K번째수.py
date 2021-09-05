def solution(array, commands):
    answer = []
    for i in commands:
        i,j,k= i[0],i[1],i[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)