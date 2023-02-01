from collections import deque

def differenceOnlyOneChar(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
           cnt +=1
    if cnt == 1:
        return True
    else:
        return False

def makeGraph(graph):
    for g in graph:
        for gg in graph:
            if differenceOnlyOneChar(g, gg):
                graph[g].add(gg)
                graph[gg].add(g)
    return graph

def bfs(graph, begin, target):
    queue = deque()
    visited = set()
    queue.append((begin, 0))
    visited.add(begin)
    while queue:
        now, turn = queue.popleft()
        if now == target:
            return turn
        for g in graph[now]:
            if g not in visited:
                queue.append((g, turn + 1))
                visited.add(g)
    return 0


def solution(begin, target, words):
    answer = 0
    words.append(begin)
    graph = {word: set() for word in words}
    makeGraph(graph)
    answer = bfs(graph, begin, target)
    return answer

begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))

