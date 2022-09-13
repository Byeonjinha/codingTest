def solution(genres, plays):
    answer = []
    musicDic = {}
    musicTime = {}
    for i in range(len(genres)):
        if genres[i] not in musicDic:
            musicDic[genres[i]] = [[plays[i],i]]
            musicTime[genres[i]] = plays[i]
        else:
            musicDic[genres[i]].append([plays[i],i])
            musicTime[genres[i]] += plays[i]
    for i in musicDic.items():
        musicDic[i[0]] = sorted(i[1] , key = lambda x:(-x[0],x[1]))
    while len(musicTime) != 0 :
        longestMusic = max(musicTime)
        longestMusicItem = max(musicTime.values())
        for k in musicTime:
            if musicTime[k] == longestMusicItem:
                longestMusic = k
        musicTime.pop(longestMusic)
        musicCount = 0 
        for music in musicDic[longestMusic]:
            musicCount += 1
            answer.append(music[1])
            if musicCount == 2 :
                break
    return answer