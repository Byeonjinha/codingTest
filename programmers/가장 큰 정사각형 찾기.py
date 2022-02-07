def solution(board):
    new_list = list(map(list, zip(*board)))
    answer = []
    for i in range(len(board)):
        for i2 in range(len(board[i])):
            if (board[i][i2]) == 1:
                print(i,i2,"i,i2")
                count=1
                a=True
                try:
                    while a==True:
                        count+=1
                        for j in range(i, i+count):
                            for j2 in range(i2, i2+count):
                                if board[j][j2] !=1:
                                    count-=1
                                    a=False
                                    break
                except:
                    print("?",(count-1)**2)
                    answer.append((count-1)**2)
    print(answer)

    answer = max(answer)
    return answer

board =[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
solution(board)