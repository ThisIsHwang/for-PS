
arr = [4,4,4,3,3]

from collections import deque

def solution(arr):
    answer = deque()
    for a in arr:
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
    return list(answer)

print(solution(arr))