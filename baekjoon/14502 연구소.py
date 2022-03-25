from collections import deque
import sys
import copy
def solution(board):
    select_wall(0,0)
    answer = 0
    for i in range(len(board)):
        print(board [i])
    return answer


# 벽 선택하기
def select_wall(start,count):
    global max_value
    if count == 3 : # 종료조건, 벽 3개 선택 완료
        sel_NM = copy.deepcopy(board) # deepcopy로 벽이 선택된 배열 복사
        for r in range(N): # 바이러스 퍼트리기
            for c in range(M):
                bfs(r, c, sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM) # clean 지역 count
        max_value = max(max_value,safe_counts)
        return True
    else:
        for i in range(start, N * M):  # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if board[r][c] == 0:  # 안전영역인 경우 벽으로 선택가능
                board[r][c] = 1  # 벽으로 변경
                select_wall(i, count + 1)  # 벽선택
                board[r][c] = 0
    print(max_value,"?")

def bfs(i,j,  board):  # 출발지, 도착지, table(9999로 초기화한 지도), board(기존 지도), c(자원에 들어가는 비용) 매개변수
    dx = [-1, 1, 0, 0]  #
    dy = [0, 0, -1, 1]  # 상하좌우를 담아줌
    x = i
    y = j  # x,y  좌표 담아줌

    n = len(board)  # 전체 지도 크기  y =  높이가  6
    m = len(board[0])  # x = 너비 10
    if board[j][i] ==0 or board[j][i] ==1:
        return
    else:
        q = deque()  # 자료 형태 좌우로 뽑아지고, 좌우로 넣을 형태
        q.append((x, y))  # 튜플형태로 x, y를 집어넣음
        while q:  # q는 deque 자료구조인데 그 자료구조에 자료가 없을 때까지
            x, y = q.popleft()  # x, y를 뽑아냄
            for i in range(4):  # 4방향으로 계산
                nx = x + dx[i]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
                ny = y + dy[i]
                if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                    continue
                if board[nx][ny] == 1 or board[nx][ny]==2:  # 벽이면  continue
                    continue
                elif board[nx][ny] == 0:  # 0감염가능하면
                    board[nx][ny] = 2  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    q.append((nx, ny))
        return 0 # end 좌표를 table에서 찾은 값
board= []
max_value = 0
N, M =  map(int,sys.stdin.readline().split())
for i in range(M):
    Map = list(map(int,sys.stdin.readline().split()))
    board.append(Map)
solution(board)