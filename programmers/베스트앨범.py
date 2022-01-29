from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(lambda:0)
    total_list = defaultdict(lambda: [])
    for i in range(len(genres)):
        genre_dic[genres[i]] += plays[i]
        total_list[genres[i]].append((plays[i],i))
    genre_dic = sorted(genre_dic.items(), key=lambda  x:x[1], reverse=True)
    print(genre_dic)
    print(total_list)
    for i in total_list:
        total_list[i] = sorted(total_list[i], key=lambda  x:x[0]    , reverse= True)[:2]
    while len(genre_dic) >0:
        genre_max   = genre_dic.pop(0)
        for t in total_list:
            if t == genre_max[0]:
                if len(total_list[t]) > 1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])
    print(answer)

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)