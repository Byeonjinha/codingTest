
def check(m,n,board):
    temp = [[0 for _ in range(n)] for i in range(m)]
    key = 0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j]!=None and board[i][j]==board[i][j+1]!=None and board[i][j]==board[i+1][j+1]!=None:
                temp[i][j]=1
                temp[i+1][j]=1
                temp[i][j+1]=1
                temp[i+1][j+1]=1
                key+=1
    return temp,board,key


def turtlim(m,n,temp,board):
    for i in range(m):
        for j in range(n):
            if temp[i][j] ==1:
                board[i][j] = None
    None_count=[]
    count=0
    for j in range(n):
        for i in range(m):
            if board[i][j] == None:
                count+=1
        None_count.append(count)
        count=0
    y=max(None_count)
    for i2 in range(y):
        for j in range(n):
           for i in range(m-1):                                   #왜 오류가안나지
                if board[m-i-1][n-j-1]==None:
                    board[m - i - 1][n - j - 1] = board[m - i - 2][n - j - 1]
                    board[m - i - 2][n - j - 1] = None
    return board

def solution(m, n, board):
    key=1
    for i in range(len(board)):
        board[i]=list(board[i])          #리스트화
    while key!=0:

        temp, board, key =check(m,n,board)
        board = turtlim(m, n, temp, board)

    count=0
    for i in range(len(board)):
        count+=(board[i].count(None))

    return count


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m, n, board)