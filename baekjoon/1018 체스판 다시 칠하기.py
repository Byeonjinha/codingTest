import copy
import sys
answer=[]
def white(board2):
    count=0
    for i in range(len(board2)):
        for j in range(len(board2[i])):
            if i%2==1 and j%2==1 and (board2[i][j])=='B':
                count+=1
            if i%2==0 and j%2==0 and (board2[i][j])=='B':
                count+=1
            if i%2==1 and j%2==0 and (board2[i][j])=='W':
                count+=1
            if i%2==0 and j%2==1 and (board2[i][j])=='W':
                count+=1
    answer.append(count)

def black(board2):
    count=0
    for i in range(len(board2)):
        for j in range(len(board2[i])):
            if i%2==1 and j%2==1 and (board2[i][j])=='W':
                count+=1
            if i%2==0 and j%2==0 and (board2[i][j])=='W':
                count+=1
            if i%2==1 and j%2==0 and (board2[i][j])=='B':
                count+=1
            if i%2==0 and j%2==1 and (board2[i][j])=='B':
                count+=1
    answer.append(count)


paint=[]
temp=[]
board=[]
board2=[]
M,N = map(int,sys.stdin.readline().split())
for i in range(M):
    p=(sys.stdin.readline().split())
    for j in p[0]:
       temp.append(j)
    paint.append(copy.deepcopy(temp))
    temp.clear()


for i in range(0,N-7):
    for j in range(0,M-7):
        for i2 in range(8):
            for j2 in range(8):
                board.append(paint[j+j2][i+i2])
            board2.append(copy.deepcopy(board))
            board.clear()
        white(board2)
        black(board2)
        board2.clear()
print(min(answer))
# board.append('%-0.8s'%q[i][0])
# print(board)
# white(paint)
# black(paint)