from collections import Counter

O = 0
X = 0 

def checkC(board, y):
    global O,X
    checkO = True
    checkX = True
    for nx in range(len(board)):
        if board[y][nx] != "O":
            checkO = False
        if board[y][nx] != "X":
            checkX = False
    if checkO:
        O += 1
    if checkX:
        X += 1

def checkR(board, x):
    global O,X
    checkO = True
    checkX = True
    for nx in range(len(board)):
        if board[nx][x] != "O":
            checkO = False
        if board[nx][x] != "X":
            checkX = False
    if checkO:
        O += 1
    if checkX:
        X += 1
def checkDiagonal(board):
    global O, X
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        O += 1
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        O += 1
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        X += 1
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        X += 1
def solution(board):
    global O, X
    answer = 1
    newBoard = []
    for y in range(len(board)):
        newBoard.extend(board[y])
        checkC(board,y)
        checkR(board,y)
    checkDiagonal(board)
    countDict = Counter(newBoard)
    if countDict["O"] < countDict["X"] or countDict["O"] > ( countDict["X"] + 1) :
        return 0
    if ( O + X ) > 1:
        print(O, X, countDict["O"], countDict["X"])
        if (O == 2 and X == 0) and (countDict["O"] - countDict["X"]) == 1:
            return 1
        return 0

    if X == 1 and countDict["O"] > countDict["X"]:
        return 0
    if O == 1 and countDict["O"] == countDict["X"]:
        return 0
    return answer