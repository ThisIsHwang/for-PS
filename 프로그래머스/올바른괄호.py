from collections import deque
def solution(s):
    answer = True
    queue = list()#deque()
    for ss in s:
        if ss == "(":
            queue.append(ss)
        else:
            if queue[-1:] != ["("]:
                answer = False
                break
            queue.pop()
    if len(queue) > 0:
        return False
    return answer

s = "(()("
print(solution(s))