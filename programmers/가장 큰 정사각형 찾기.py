def solution(board):
    new_list = list(map(list, zip(*board)))
    answer = []
    print(new_list)
    for i in range(len(board)):
        for i2 in range(len(board[i])):
            a = False
            if (board[i][i2]) == 1:
                    for j in range(i,len(board)):
                        count =1
                        if board[j][i2] != 1:
                            break
                        for j2 in range(i2,len(new_list[i2])):
                            count+=1
                            print(i2,j2)
                            if new_list[i2][j2]!=1:
                                break
                        answer.append(count**2)

    print(answer)
    answer = max(answer)
    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
solution(board)