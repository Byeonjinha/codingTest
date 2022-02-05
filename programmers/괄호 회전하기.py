
def solution(s):
    t_count=0
    for i in range(len(s)):
        count1 = 0
        count2 = 0
        count3 = 0
        s3 = s[i:]+s[:i]
        for j in range(len(s3)):
            if s3[j]=="[":
                count1+=1
            elif s3[j]=="]":
                count1-=1
            elif s3[j]=="(":
                count2+=1
            elif s3[j]==")":
                count2-=1
            elif s3[j]=="{":
                count3+=1
            elif s3[j]=="}":
                count3-=1

            if count1 < 0:
                break
            elif count2 <0:
                break
            elif count3 <0 :
                break
        if count1==0 and count2==0 and count3==0:
            t_count+=1

    answer = t_count
    print(answer)
    return answer

s= "{{{}"
solution(s)