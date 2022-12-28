from collections import deque

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def checkInDegree(graph):
    inDegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            inDegree[j] += 1
    return inDegree

def getDistance(graph):
    distance = [0] * (n + 1)
    for ii in range(1, n + 1):
        visited = [False] * (n + 1)
        q = deque([ii])
        visited[ii] = True
        tempDistance = 0
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    tempDistance += 1
        distance[ii] = tempDistance
    return distance

def solution(n, results):
    answer = 0
    graph = {i :set() for i in range(1, n +1)}
    for r in results:
        graph[r[0]].add(r[1])
    isVisited = set()
    while True:
        inDegree = checkInDegree(graph)
        distance = getDistance(graph)
        if len(isVisited) == n:
            break

        cnt = 0
        for i in range(1, len(inDegree)):
            if inDegree[i] == 0 and i not in isVisited:
                cnt += 1

        if cnt == 1:
            answer += 1

        for i in range(1, n + 1):
            if inDegree[i] == 0 and distance[i] == max(distance) and i not in isVisited:
                print(i)
                graph[i] = set()
                isVisited.add(i)

    return answer

solution(n, results)