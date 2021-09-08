import sys

n =int(sys.stdin.readline())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))            #입력받은 그래프를 list화해서 저장
count1=0                                            #칸수 카운팅하기 위한변수
def dfs(x,y):
    global count1
    if x <= -1 or x >= n or y <= -1 or y >=n:       # 칸수 넘어가면 False 리턴
        return False
    if graph[x][y] == 1:                            #그래프좌표가 1이면
        graph[x][y] =0                              #그래프좌표를 0으로 만들고
        count1+=1                                   #카운팅을하고
        dfs(x-1,y)                                  #왼쪽
        dfs(x,y-1)                                  #밑
        dfs(x+1,y)                                  #오른쪽
        dfs(x,y+1)                                  #위 재귀식진행
        return True                                 #True를 리턴
    return False

result=0
countlist=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j) ==True:
            countlist.append(count1)
            count1=0
            result+=1

print(result)
countlist.sort()
for i in countlist:
    print(i)
