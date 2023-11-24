import sys

sys.setrecursionlimit(10 ** 6)

answer = "impossible"

lowestWord = "z"

goalY, goalX = 0, 0
height, width = 0, 0

dy, dx = [1, 0, 0 , -1], [0, -1, 1, 0]
moves = ["d", "l", "r", "u"]

def validate(y, x, moveCount, move):
    global goalY, goalX, lowestWord
    
    if (abs(goalY - y) + abs(goalX - x)) > moveCount:
        return False
    if (abs(goalY - y) + abs(goalX - x)) % 2 != moveCount % 2:
        return False
    
    words = [lowestWord, move]
    words.sort()
    if len(move) <= len(words[0]) and move != words[0]:
        return False
    lowestWord = move
    
    return True

def locationValidate(y, x):
    global height, width
    return 0 <= y < height and 0 <= x < width

def dfs(y, x, moveCount, move):
    global goalY, goalX, moves, answer
    
    if not validate(y, x, moveCount, move):
        return
    
    if moveCount == 0:
        if y == goalY and x == goalX:
            if answer == "impossible": answer = move
            else:
                answers = [answer, move]
                answers.sort()
                answer = answers[0]
        return 
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        nextMove = moves[d]
        if locationValidate(ny, nx):
            dfs(ny, nx, moveCount - 1, move + nextMove)
    return

def solution(n, m, x, y, r, c, k):
    global answer, goalY, goalX, width, height, moves
    
    goalY, goalX = r - 1, c - 1
    height, width = n, m 
    startY, startX = x - 1, y - 1
    
    for d in range(4):
        ny = startY + dy[d]
        nx = startX + dx[d]
        nextMove = moves[d]
        if locationValidate(ny, nx):
            dfs(ny, nx, k - 1, nextMove)

    return answer