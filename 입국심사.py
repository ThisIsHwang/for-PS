from typing import Union, Any

n = 6
times = [7, 10]

def solution(n, times):

    low = 1
    high = max(times) * n

    while low <= high:
        mid: int = (low + high) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break

        if cnt >= n:
            high = mid - 1
        else:
            low = mid + 1
    return low

        #tempAnswer = max(7 * a, 10 * (n-a))



a = solution(n, times)
print(a)