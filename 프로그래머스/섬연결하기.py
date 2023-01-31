import heapq

def solution(n, costs):
    answer = []
    graph = {i : dict() for i in range(n)}
    for cost in costs:
        graph[cost[0]][cost[1]] = cost[2]
        graph[cost[1]][cost[0]] = cost[2]

    visited = set()
    distances = []

    now = 0

    heapq.heappush(distances, (0, 0, now))
    while len(answer) != n:
        dis, before, now = heapq.heappop(distances)
        if now not in visited:
            visited.add(now)
            answer.append((before, now, dis))
        else:
            continue
        for g in graph[now]:
            if g not in visited:
                heapq.heappush(distances, (graph[now][g], now, g))

    distance = 0
    for i in range(len(answer)):
        distance += answer[i][2]
    return distance

n = 7
costs = [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]]
print(solution(n, costs))