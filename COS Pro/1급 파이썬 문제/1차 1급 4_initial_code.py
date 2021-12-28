#You may use import as below.
#import math

def solution(num):
    num += 1
    #for statemenet
    # answer = ''
    # for x in str(num):
    #     if x == '0' : x = '1'
    #     answer +=x
    # return answer
    #comprehension (expression)
    answer = ''.join('1' if x == '0' else x for x in str(num))
    return answer


    # digit = 1
    # while num // digit % 10 == 0:
    #     num += digit
    #     digit *= 10
    # return num

#The following is code to output testcase.
num = 9949999;
ret = solution(num  )

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")