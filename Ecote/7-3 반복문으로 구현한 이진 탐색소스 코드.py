def solution(sortedArray, findValue):
    start= 0
    end = len(sortedArray)
    print(start,end)
    while start <= end:
        mid = (start + end) // 2
        if sortedArray[mid] == findValue:
            return mid
        elif sortedArray[mid] > findValue:
            end = mid - 1
        else:
            start = mid + 1
    return -1


sortedArray=	[1, 2, 5, 7, 10, 15, 18, 20]
findValue = 15
solution(sortedArray,findValue)