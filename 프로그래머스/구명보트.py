from collections import deque
def solution(people, limit):
    answer = 0

    queue = deque(sorted(people))

    while queue:
        if len(queue) == 1:
            answer += 1
            break
        front = queue.popleft()
        back = queue.pop()

        if front + back <= limit:
            answer += 1
        else:
            queue.appendleft(front)
            answer += 1
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))