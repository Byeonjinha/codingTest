import math
from collections import deque

def solution(board,c):
    table = [[math.inf for _ in range(len(board[0]))] for _ in range(len(board))]
    print(table)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                start = [i, j]
            if board[i][j] == 3:
                end = [i, j]
    bfs(start,end ,table,board)
    print(start, end)

def bfs(start,end ,table,board):
    x= start[0]
    y= start [1]
    n= len(board)
    m= len(board[0])

    return board[n-1][m-1]



board = [ [0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]]
c=1
solution(board, c)
'''
10 10
1111111111
1000000001
1110000111
1100000101
1111011101
0010110101
0010110000
1110111111
1110111111
0000000001
'''
