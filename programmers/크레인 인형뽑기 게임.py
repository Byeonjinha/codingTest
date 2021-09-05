baguni=[]
def solution(board, moves):
    for i in moves:
        try:
            for i2 in range(30):
                if board[i2][i-1]!=0:
                    baguni.append(board[i2][i-1])
                    board[i2][i - 1]=0
                    break
        except:
            pass
    return turtrim(baguni)

def turtrim(baguni):
    count=0
    i=0
    for i3 in range(30):
        while True:
            try:
                if baguni[i]==baguni[i+1]:
                    count += 2
                    del baguni[i]
                    del baguni[i]
                i+=1
            except:
                pass
            if i>len(baguni)-2:
                i=0
                break
    return count





board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)