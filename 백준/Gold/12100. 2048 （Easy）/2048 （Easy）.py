import sys, copy
sys.setrecursionlimit(10 ** 5)
n = int(sys.stdin.readline())

answer = 0
check = []
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def trans_left_right(graph):
    for y in range(len(graph)):
        graph[y] = list(reversed(graph[y]))
    return graph

def zero_management(graph):
    for y in range(len(graph)):
        for x in range(len(graph[y]) - 1):
            if graph[y][x] == 0:
                graph[y][x] = "empty"
                continue
        while "empty" in graph[y]:
            graph[y].remove("empty")
            graph[y].append(0)
    return graph


def find_answer(graph):
    global answer
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            answer = max(answer, graph[y][x])
    return


def sum_left(graph):
    graph = zero_management(graph)
    for y in range(len(graph)):
        flag = False
        for x in range(len(graph[y]) - 1):
            if flag:
                flag = False
                continue
            if graph[y][x] == graph[y][x + 1]:
                graph[y][x] = graph[y][x] + graph[y][x + 1]
                graph[y][x + 1] = "empty"
                flag = True

        while "empty" in graph[y]:
            graph[y].remove("empty")
            graph[y].append(0)

    return graph

def sum_right(graph):
    graph = trans_left_right(graph)
    graph = zero_management(graph)
    for y in range(len(graph)):
        flag = False
        for x in range(len(graph[y]) - 1):
            if flag:
                flag = False
                continue
            if graph[y][x] == graph[y][x + 1]:
                graph[y][x] = graph[y][x] + graph[y][x + 1]
                graph[y][x + 1] = "empty"
                flag = True

        while "empty" in graph[y]:
            graph[y].remove("empty")
            graph[y].append(0)
    graph = trans_left_right(graph)
    return graph

def sum_up(graph):
    graph = list(map(list, zip(*graph)))
    graph = trans_left_right(graph)
    graph = zero_management(graph)
    for y in range(len(graph)):
        flag = False
        for x in range(len(graph[y]) - 1):
            if flag:
                flag = False
                continue
            if graph[y][x] == graph[y][x + 1]:
                graph[y][x] = graph[y][x] + graph[y][x + 1]
                graph[y][x + 1] = "empty"
                flag = True

        while "empty" in graph[y]:
            graph[y].remove("empty")
            graph[y].append(0)
    graph = trans_left_right(graph)
    graph = list(map(list, zip(*graph)))
    return graph

def sum_down(graph):
    graph = list(map(list, zip(*graph)))
    graph = zero_management(graph)
    for y in range(len(graph)):
        flag = False
        for x in range(len(graph[y]) - 1):
            if flag:
                flag = False
                continue
            if graph[y][x] == graph[y][x + 1]:
                graph[y][x] = graph[y][x] + graph[y][x + 1]
                graph[y][x + 1] = "empty"
                flag = True

        while "empty" in graph[y]:
            graph[y].remove("empty")
            graph[y].append(0)
    graph = list(map(list, zip(*graph)))
    return graph


def dfs(graph, count):
    global check
    left_graph, right_graph, up_graph, down_graph = copy.deepcopy(graph), copy.deepcopy(graph), copy.deepcopy(graph), copy.deepcopy(graph)

    if count == 5:
        find_answer(graph)
        return
    if (graph, count) in check:
        return
    find_answer(graph)
    check.append((graph, count))

    left_graph = sum_left(left_graph)
    right_graph = sum_right(right_graph)
    up_graph = sum_up(up_graph)
    down_graph = sum_down(down_graph)

    # print("left")
    # for i in left_graph:
    #     print(i)
    # print()
    # print("right")
    # for i in right_graph:
    #     print(i)
    # print()
    #
    # print("up")
    # for i in up_graph:
    #     print(i)
    # print()
    #
    # print("down")
    # for i in down_graph:
    #     print(i)
    # print()
    dfs(left_graph, count + 1)
    dfs(right_graph, count + 1)
    dfs(up_graph, count + 1)
    dfs(down_graph, count + 1)

    # print(left_graph)



dfs(graph, 0)

print(answer)