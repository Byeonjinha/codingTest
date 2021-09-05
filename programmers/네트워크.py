from collections import  deque
answer=0
def bfs(graph,start,visited):
    global answer
    visited[start]=True
    queue = deque([graph[start]])
    while queue:
        v=queue.popleft()                           #꺼내기
        for i in range(len(v)):                 #연결되있는지 전수조사
            for j in range(len(v)):            #연결되있는지 전수조사
                if i!=j and v[j]==1:         # 나자신 외에 연결되어 있으면
                    if not visited[j]:              # 방문을 안했으면
                        visited[j]=True             # 방문표기하고
                        queue.append(graph[j])      # 집어넣음
    answer+=1
    print(visited)
    if False in visited:                             #방문안한 곳 방문
        bfs(graph, visited.index(False),visited)

def solution(n,computers):
    global answer
    visited = [False] * n
    bfs(computers,0,visited)
    print(answer)
    return answer
