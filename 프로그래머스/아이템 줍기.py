from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    points = set()
    inbound = set()
    graph = dict()
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for r in rectangle:
        tx = -1
        ty = -1
        tempPoints = set()
        for x in range(r[0] + 1, r[2] + 1):
            tempPoints.add((x, r[1], x - 1, r[1]))
            tempPoints.add((x - 1, r[1], x, r[1]))

        for x in range(r[0] + 1, r[2] + 1):
            tempPoints.add((x, r[3], x - 1, r[3]))
            tempPoints.add((x - 1, r[3], x, r[3]))

        for y in range(r[1] + 1, r[3] + 1):
            tempPoints.add((r[0], y, r[0], y - 1))
            tempPoints.add((r[0], y - 1, r[0], y))

        for y in range(r[1] + 1, r[3] + 1):
            tempPoints.add((r[2], y - 1, r[2], y))
            tempPoints.add((r[2], y, r[2], y -1))

        for x in range(r[0], r[2] + 1):
            for y in range(r[1], r[3] + 1):
                if tx == -1 or ty == -1:
                    tx = x
                    ty = y
                    continue

                for xx, yy in zip(dx, dy):
                    if r[0] <= x + xx <= r[2] and r[1] <= y + yy <= r[3]:
                        if (x, y, x + xx, y + yy) not in tempPoints and (x + xx, y + yy, x, y) not in tempPoints:
                            inbound.add((x, y, x + xx, y + yy))
                            inbound.add((x + xx, y + yy, x, y))

        points.update(tempPoints)


    for x, y, x2, y2 in points:
        if (x, y, x2, y2) not in inbound:
            if (x, y) in graph:
                graph[(x,y)].add((x2, y2))
            else:
                graph[(x,y)] = set()
                graph[(x, y)].add((x2, y2))
            if (x2, y2) in graph:
                graph[(x2,y2)].add((x, y))
            else:
                graph[(x2, y2)] = set()
                graph[(x2, y2)].add((x, y))
    queue = deque()
    isVisited = set()
    queue.append((characterX, characterY, 0))
    isVisited.add((characterX, characterY))

    while queue:
        x, y, turn = queue.popleft()
        if x == itemX and y == itemY:
            return turn
        for g in graph[(x, y)]:
            if g not in isVisited:
                queue.append((g[0], g[1], turn + 1))
                isVisited.add((g[0], g[1]))

    return 0

rectangle = [[2,1,7,5],[6,4,10,10]]
characterX = 3
characterY = 1
itemX = 7
itemY = 10

print(solution(rectangle, characterX, characterY, itemX, itemY))

