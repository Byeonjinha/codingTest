def func_a(string, length):   #2021/12/26 0을 앞에 채워 길이를 맞추는 작업
    padZero = ""
   # padSize = @@@
    padSize = length - len(string)
    for i in range(padSize):
        padZero += "0"
    return padZero + string

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length)
    
    hamming_distance = 0
    for i in range(max_length):
       # if @@@: ->    binaryA의 i 번째 와 binaryB의 i 번째가 같지않을때 hamming 거리가 증가함
        if binaryA[i] != binaryB[i]:
            hamming_distance += 1
    return hamming_distance

#The following is code to output testcase.
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")