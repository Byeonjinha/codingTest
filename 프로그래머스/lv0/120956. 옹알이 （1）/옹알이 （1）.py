def solution(babbling):
    answer = 0
    dic = {"aya":0, "ye":0, "woo":0, "ma":0}
    for word in babbling:
        while word[0] == "a" or word[0] == "y" or word[0] == "w" or word[0] == "m" :
            if word[0:3] == "aya":
                word = word[3:]
            elif word[0:2] == "ye":
                word = word[2:]
            elif word[0:3] == "woo":
                word = word[3:]
            elif word[0:2] == "ma":
                word = word[2:]
            else:
                break
            if len(word) == 0:
                answer += 1
                break
    return answer