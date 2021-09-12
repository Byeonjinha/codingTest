import copy

board2=[]
def bbusim(i,board2):
    for x in range(i[1],i[3]+1):
        for y in range(i[2],i[4]+1):
            board2[x][y]= board2[x][y] -i[5]
    return board2
def gochim(i,board2,board):
    for x in range(i[1],i[3]+1):
        for y in range(i[2],i[4]+1):
            board2[x][y]+=i[5]
    return board2


def solution(board, skill):
    count1 = 0
    board2=copy.deepcopy(board)
    for i in skill:
        if i[0]==1:
            board2=bbusim(i,board2)
        elif i[0]==2:
            board2=gochim(i,board2,board)

    for k in range(len(board2)):
        for k2 in range(len(board2[k])):
            if board2[k][k2]>0:
                count1+=1
    print(count1)
    return count1

board =[[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
solution(board, skill)