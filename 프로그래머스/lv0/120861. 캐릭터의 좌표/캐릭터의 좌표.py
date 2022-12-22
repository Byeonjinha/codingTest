def findDirection(direction):
    if direction == "up":
        return 0
    elif direction == "down":
        return 1
    elif direction == "left":
        return 2
    else :
        return 3
def solution(keyinput, board):
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    y, x = 0, 0
    for i in keyinput:
        direction = findDirection(i)
        ny = y + dy[direction]
        nx = x + dx[direction]
        if ny > board[1] // 2 or  ny < -(board[1] // 2) or nx > board[0] // 2 or nx < -(board[0] // 2) :
            print("continue")
            continue
        y, x = ny, nx
        
    return [x, y]