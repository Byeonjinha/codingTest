def checkBabbling(word, previousWord):
    while word[:3] == "aya" and previousWord != "aya" or word[:2] == "ye"  and previousWord != "ye" or word[:3] == "woo"  and previousWord != "woo" or word[:2] == "ma"  and previousWord != "ma":
        if word[:3] == "aya" and previousWord != "aya":
            previousWord = "aya"
            word =  word.replace("aya", "", 1)
            checkBabbling(word, "aya")
        elif word[:2] == "ye"  and previousWord != "ye":
            previousWord = "ye"
            word =  word.replace("ye", "", 1)
            checkBabbling(word, "ye")
        elif word[:3] == "woo"  and previousWord != "woo":
            previousWord = "woo"
            word = word.replace("woo", "", 1)
            checkBabbling(word, "woo")
        elif word[:2] == "ma"  and previousWord != "ma":   
            previousWord = "ma"
            word = word.replace("ma", "", 1)
            checkBabbling(word, "ma")
    if len(word) == 0 :
        return 1
    return 0

def solution(babbling):
    answer = 0
    for word in babbling:
        answer += (checkBabbling(word, ""))
    return answer