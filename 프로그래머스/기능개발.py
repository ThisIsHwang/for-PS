progresses = [96, 95, 96, 93]
speeds = [1, 1, 1, 1]

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        tempDeque = deque()
        needDays = (100 - progresses[0]) // speeds[0]
        if progresses[0] + needDays * speeds[0] < 100:
            needDays += 1
        tempDeque.append(progresses.popleft())
        speeds.popleft()

        cnt = 0
        flag = True
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i] * needDays

            if progresses[i] >= 100 and flag:
                cnt += 1
                tempDeque.append(progresses[i])
            else:
                flag = False

        for i in range(cnt):
            progresses.popleft()
            speeds.popleft()
        answer.append(len(tempDeque))
    return answer

print(solution(progresses, speeds))