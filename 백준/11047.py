import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

coin_costs = deque([])
for _ in range(N):
    coin_costs.appendleft(int(sys.stdin.readline()))
answer = 0
for cost in coin_costs:
    temp = K // cost
    if temp:
        K = K % cost
        answer += temp

print(answer)
