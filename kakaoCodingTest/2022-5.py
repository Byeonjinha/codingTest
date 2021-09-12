
import sys
read = sys.stdin.readline
count=[]

def dfs(v,    visit_list,visit_list2,graph,n,count):
    count+=info[v]

    visit_list2[v] = 0
    for i in range(1, n + 1):
        if visit_list2[i] == 1 and graph[v][i] == 0:
            dfs(i, visit_list,visit_list2,graph,n,count)
    return count
def solution(info, edges):
    n = len(info)                        #노드 수
    m = len(edges)                       #간선 수
    v = 1                               #시작
    graph = [[0] * (n + 1) for _ in range(n + 1)]         #그래프 초기화

    visit_list = [0] * (n + 1)                           #방문여부
    visit_list2 = [0] * (n + 1)                          #방문여부
    for i in range(m):
        a, b = edges[i][0],edges[i][1]
        graph[a][b] = graph[b][a] = 1                      #그래프그리기
    count=0
    count =dfs(v, visit_list,visit_list2,graph,n,count)
    print(count)


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

solution(info, edges)