import sys
from collections import defaultdict, deque

n = int(input().rstrip())

graph = [input().rstrip() for _ in range(n)]

isVisited = set()
Danjis = []

number_of_complex = 0

#여기서 너는 단지 내의 집을 return 해야
def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])
    isVisited.add((start))
    cnt = 0
    while queue:
        cnt += 1
        popped_y, popped_x = queue.popleft()
        for y, x in zip(dy, dx):
            n = len(graph)
            if 0 <= popped_y + y < n and 0 <= popped_x + x < n and (popped_y + y, popped_x + x) not in isVisited and graph[popped_y + y][popped_x + x] == "1":
                isVisited.add((popped_y + y, popped_x + x))
                queue.append((popped_y + y, popped_x + x))
    return cnt

for i, row in enumerate(graph):
    for ii, cell in enumerate(graph[i]):
        if cell == '1' and (i, ii) not in isVisited:
            Danjis.append(bfs((i, ii)))



print(len(Danjis))
for value in sorted(Danjis):
    print(value)