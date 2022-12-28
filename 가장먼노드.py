from collections import deque

def makeGraph(vertex):
    for v in vertex:
        graph[v[0]].add(v[1])
        graph[v[1]].add(v[0])

visited = [False] * (n + 1)
depth = [0] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                depth[i] = depth[v] + 1

graph = {i :set() for i in range(1, n +1)}

def solution(n, edge):
    makeGraph(edge)
    bfs(1)
    tempList = [d for d in depth if max(depth) == d]
    answer = len(tempList)
    return answer









