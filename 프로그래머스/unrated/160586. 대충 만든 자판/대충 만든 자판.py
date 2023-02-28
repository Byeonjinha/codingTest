dict = {}


def solution(keymap, targets):
    global dict
    answer = []
    for words in keymap:
        for wordIdx in range(len(words)):
            word = words[wordIdx]
            if word not in dict:
                dict[word] = wordIdx + 1
            else:
                minIdx = min(wordIdx + 1, dict[word])
                dict[word]= minIdx
    for targetsWords in targets:
        totalIdx = 0
        flag = False
        for targetWordIdx in range(len(targetsWords)):
            alpha = targetsWords[targetWordIdx]
            if alpha in dict:
                totalIdx += dict[alpha]
            else:
                answer.append(-1)
                flag = True
                break
        if flag:
            continue
        answer.append(totalIdx)
        
    return answer