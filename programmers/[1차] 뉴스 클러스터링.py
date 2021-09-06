from string import ascii_lowercase
from itertools import product

alpha= ascii_lowercase
alphalist =  list(product(alpha,repeat =2))
alphalist2 = []
for i in alphalist:
    alphalist2.append(''.join(i))

def mookie(str1):
    ziphap=[]
    for i in range(len(str1)-1):
        if str1[i]+str1[i+1] in alphalist2:
            ziphap.append(str1[i]+str1[i+1])
    return ziphap
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str3=[]
    str4=[]
    str1 = mookie(str1)
    str2 = mookie(str2)
    print(str1,str2)
    print(len(str1),len(str2))
    if len(str1)==0 and len(str2)==0:
        return 65536
    else:
        for i in range(len(str1)):
            if str1[i] in str2:
                str3.append(str1[i])
                str2.remove(str1[i])

        str4=str1+str2

    answer = int(len(str3)/len(str4)*65536)

    return answer

str1 = 'aa1+aa2'
str2 = 'AAAA12'
solution(str1, str2)