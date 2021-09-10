import math
from collections import deque

def solution(board):

    def bfs(start):
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]          # n,n 테이플  무한대로 초기화
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]                                                  # 움직이는 각 좌표값 저장
        # print(start)                                                                   #스타트값이 왜 0,0,0,2 ? 0,0,0,3?
        queue = deque([start])                                                              # start 를  deque 로 만듬

        table[0][0] =0                                                                      #출발값을 0으로 만듬

        while queue:                                                                        #queue 에 값이 없을 때 까지
            y,x,cost,head = queue.popleft()                                                 #queue 출력
            for idx, (dy,dx) in enumerate(dirs):                                            # dirs list 안의 자료  index 와 값을 튜플로 묶어서 list 로 출력
                ny,nx=y+dy,x+dx                                                             #각 현재좌표 x,y 값에  각각의 dy,dx좌표로 이동한 값을 더해서 ny, nx 라는 이동한 위치 변수를 만들어줌
                if idx != head:                                                             # 인덱스랑 head(방향)이 같지않으면
                    n_cost = cost +600                                                      #n_cost 현재비용은  600이 더해짐
                else:
                    n_cost = cost +100                                                      # 같으면 100이 더해짐
                if 0<= ny < len(board) and 0<= nx <len(board) and board[ny][nx] == 0 and table[ny][nx] >n_cost:      # 현재값이 지도를 벗어나지 않을경우 , 좌표값이 비용보다  더클 경우에
                    table[ny][nx] = n_cost                                                                           # table 의 현재 좌표값 비용은 계산된 비용이됨
                    queue.append((ny,nx,n_cost,idx))                                                               # 현재 좌표값, 비용, 방향을 queue 에 다시 저장
            print(table)
        return table[-1][-1]                                                                #도착값 출력

    print(bfs((0,0,0,3)))
    # return min(bfs((0,0,0,2)),bfs((0,0,0,3)))                                               #각 진행방향이 아래 또는 오른쪽일경우 중 작은 값을 선택

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
solution(board)