import sys


#   1
# 2   3

def floyd(graph):

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):

                if graph[i][j] == 0:
                    graph[i][j] = float("inf")
                if graph[i][k] == 0:
                    graph[i][k] = float("inf")
                if graph[k][j] == 0:
                    graph[k][j] = float("inf")
                if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
graph = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    t = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(t)

floyd(graph)
for g in graph:
    for gg in g:
        if gg != float("inf"):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
