def solution(s):
    sutja =['0','1','2','3','4','5','6','7','8','9']
    count=0
    if len(list(s))==4 or len(list(s))==6:
        for i in list(s):
            if i in sutja:
                count+=1
        if len(list(s))==count:
            return True
    return False

s="a234"
solution(s)