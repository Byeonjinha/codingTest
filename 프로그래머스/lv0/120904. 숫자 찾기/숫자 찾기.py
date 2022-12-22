def solution(num, k):
    if str(k) not in str(num):
        return -1
    
    return list(str(num)).index(str(k))+1