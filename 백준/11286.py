import sys
import heapq

n = int(sys.stdin.readline())

heap = []
#heapq.heappush()
for _ in range(n):
    tWord = int(sys.stdin.readline())
    if tWord > 0:
        heapq.heappush(heap, (tWord, tWord))
    elif tWord < 0:
        heapq.heappush(heap, (-tWord, tWord))
    else:
        if not heap:
            print(0)
        else:
            tt = heapq.heappop(heap)
            print(tt[1])




