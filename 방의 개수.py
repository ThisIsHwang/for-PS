
arrows = [6, 5, 2, 7, 1, 4, 2, 4, 6]

def move(num):
    if num == 0:
        return (-1, 0)
    elif num == 1:
        return (-1, 1)
    elif num == 2:
        return (0, 1)
    elif num == 3:
        return (1, 1)
    elif num == 4:
        return (1, 0)
    elif num == 5:
        return (1, -1)
    elif num == 6:
        return (0, -1)
    elif num == 7:
        return (-1, -1)


def solution(arrows):
    answer = 0
    now = (0, 0)

    visited = set()
    visitedDir = set()

    visited.add(now)

    for arrow in arrows:
        for _ in range(2):
            temp = now
            now = (now[0] + move(arrow)[0], now[1] + move(arrow)[1])
            if now in visited and (temp, now) not in visitedDir:
                answer += 1
            visited.add(now)
            visitedDir.add((temp, (temp[0] + move(arrow)[0], temp[1] + move(arrow)[1])))
            visitedDir.add(((temp[0] + move(arrow)[0], temp[1] + move(arrow)[1]), temp))

    return answer

print(solution(arrows))