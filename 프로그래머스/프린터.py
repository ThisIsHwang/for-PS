priorities = [1, 1, 9, 1, 1, 1]

import heapq
from collections import deque

def solution(priorities, location):
    answer: int = 0
    heap = [-p for p in priorities].copy()
    heapq.heapify(heap)
    currentLocation = location

    queue = deque(priorities)
    already = False
    while not already:
        max_num = -heapq.heappop(heap)
        while True:
            if max_num != queue[0]:
                a = queue.popleft()
                queue.append(a)
                currentLocation -= 1
                if currentLocation < 0:
                    currentLocation += len(queue)
            else:
                queue.popleft()
                answer += 1
                if currentLocation == 0:
                    already = True
                    break
                currentLocation -= 1
                if currentLocation < 0:
                    currentLocation += len(queue)
                break
    return answer
location = 0

print(solution(priorities, location))