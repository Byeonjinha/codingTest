import string
def solution(n):
    threeNum = 0
    for i in range(1,n+1):
        threeNum += 1
        threeNumArray = list(str(threeNum))
        while threeNum % 3 == 0 or "3" in threeNumArray:
            if threeNum % 3 == 0 :
                threeNum += 1
                threeNumArray = list(str(threeNum))
                continue
            if "3" in threeNumArray and threeNumArray.index("3") == 0 :
                threeNumArray = ["0" for _ in range(len(threeNumArray))]
                threeNumArray[0] = "4"
                threeNum = int(''.join(threeNumArray))
            elif "3" in threeNumArray and threeNumArray.index("3") != 0 :
                threeNumArray[threeNumArray.index("3")] = str(int(threeNumArray[threeNumArray.index("3")]) + 1)
                threeNum = int(''.join(threeNumArray))
    return threeNum