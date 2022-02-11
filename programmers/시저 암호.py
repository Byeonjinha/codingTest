def solution(s, n):
    alpha_list = []
    for i in range(len(s)):
        if 97 <= ord(s[i]) <=122 :
            k =(ord(s[i])-ord('a')+ n)%26+ord('a')
            alpha_list.append(chr(k)) 
        elif 65 <= ord(s[i]) <=90 :
            k = (ord(s[i])-ord('A')+ n)%26+ord('A')
            alpha_list.append(chr(k))
        else:
            alpha_list.append(s[i])
    print(alpha_list)
    return ''.join(alpha_list)
s= "AaZz"
n= 25
solution(s,n)