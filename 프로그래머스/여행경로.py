from collections import defaultdict

def dfs(now, graph, isVisited, answer):
    if sum(v != 0 for v in isVisited.values()) == 0:
        return answer

    for g in graph[now]:
        if isVisited[(now, g)]:
            isVisited[(now, g)] -= 1
            new_isVisited = isVisited.copy()
            new_answer = answer + [g]
            result = dfs(g, graph, new_isVisited, new_answer)
            if result:
                return result
            isVisited[(now, g)] += 1
    return []

def solution(tickets):
    graph = defaultdict(list)
    isVisited = defaultdict(int)

    for t in tickets:
        isVisited[(t[0], t[1])] += 1
        graph[t[0]].append(t[1])

    for g in graph.values():
        g.sort()

    answer = ['ICN']
    return dfs('ICN', graph, isVisited, answer)
