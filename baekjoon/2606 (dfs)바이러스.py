
import sys
read = sys.stdin.readline
count=[]

def dfs(v):
    count.append(0)
    visit_list2[v] = 1
    for i in range(1, n + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
v = 1

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print(len(count)-1)
# bfs(v)