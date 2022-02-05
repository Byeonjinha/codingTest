from string import ascii_lowercase
def solution(s):
    alpha = list(ascii_lowercase)
    s= s.split(" ")
    print(s)
    answer = []
    for i in range(len(s)):
        if s[i] == "":
            answer.append(s[i])
        else:
            if s[i].lower()[0] in alpha:
                word = s[i][0].upper()+s[i].lower()[1:]
            else:
                word = s[i].lower()
            answer.append(word)
    print(answer)
    return ' '.join(answer)


s= "a a a a a a a a a a "
solution(s)