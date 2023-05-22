def solution(picture, k):
    answer = []
    for y in range(len(picture)):
        for i in range(k):
            piece = []
            for x in range(len(picture[y])):
                for j in range(k):
                    piece.append(picture[y][x])
            answer.append(''.join(piece))   
    return answer