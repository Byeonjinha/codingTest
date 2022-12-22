def solution(board):
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [-1,-1,0,1,1,1,0,-1]
    answer = 0 
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1 :
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if nx >= len(board[y]) or nx < 0 or ny >= len(board) or ny < 0 or board[ny][nx] == 1:
                        continue 
                    board[ny][nx] = 2 
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0 :
                answer += 1
    for i in board :
        print(i)
    return answer