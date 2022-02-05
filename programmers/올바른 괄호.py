def solution(s):
    a = []
    try:
        for i in range(len(s)):
            if s[i] == "(":
                a.append("(")
            if s[i] == ")":
                a.pop()
        if len(a)==0:
            return True
        else:
            return False
    except:
        return False

s="(()("
solution(s)