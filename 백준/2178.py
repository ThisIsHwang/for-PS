import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
graph = []
for i in range(n):
    s = sys.stdin.readline().strip()

    graph.append(list(s))

queue = deque()
isVisited = set()
x, y = 1, 1
x -= 1
y -= 1
queue.append((x, y, 0))
isVisited.add((x, y))
turn = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, turn = queue.popleft()
    if x == n-1 and y == m-1:
        break
    for xx, yy in zip(dx, dy):
        if 0 <= x + xx < n and 0 <= y + yy < m:
            if graph[x + xx][y + yy] == "1" and (x + xx, y + yy) not in isVisited:
                isVisited.add((x + xx, y + yy))
                queue.append((x + xx, y + yy, turn + 1))

print(turn + 1)
