res = 0
def solution(n):
    global res
    board = [0] * 15
    recursive(0,n,board)
    print(res)
    return res
def recursive(x,n,board):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        board[x] = i
        if check(x, board):
            recursive(x+1,n,board)


def check(x, board):
    for i in range(x):
        if board[x] == board[i] or abs(board[i]-board[x]) == x-i:
            return False
    return True