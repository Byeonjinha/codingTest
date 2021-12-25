#You may use import as below.
#import math

def solution(shirt_size):
    answer=[0]*6
    for i in shirt_size:
        if i == "XS":
            answer[0]+=1
        elif i =="S":
            answer[1]+=1
        elif i =="M":
            answer[2]+=1
        elif i =="L":
            answer[3]+=1
        elif i =="XL":
            answer[4]+=1
        else:
            answer[5]+=1
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")