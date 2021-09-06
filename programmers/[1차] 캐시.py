from  collections import deque
def solution(cacheSize, cities):
    cities2 = []
    for i in cities:
        if len(i)>20:
            i=len(i)/0
        if cacheSize>30:
            i=len(i)/0
        cities2.append(i.lower())

    if cacheSize==0:
        return len(cities2)*5


    cache = deque([0]*cacheSize)
    silhengsihan=0

    for i in range(len(cities2)):
        if cities2[i] in cache:
            silhengsihan+=1
            cache.remove(cities2[i])
            cache.append(cities2[i])

        else:
            silhengsihan+=5
            cache.popleft()
            cache.append(cities2[i])


    answer = silhengsihan
    return answer