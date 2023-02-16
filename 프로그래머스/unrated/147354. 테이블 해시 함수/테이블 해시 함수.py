def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    answer = 0 
    for idx in range(len(data)):
        if row_begin <= (idx + 1) <= row_end:
            tmp = 0 
            for i in data[idx]:
                tmp += i % (idx + 1) 
            answer ^= tmp
    return answer