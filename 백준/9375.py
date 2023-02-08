# 3
# eyewear sunglasses
# headgear
import sys
from collections import defaultdict
tc = int(sys.stdin.readline().strip())

while tc:
    graph = defaultdict(set)
    tc -= 1
    n = int(sys.stdin.readline())

    for _ in range(n):
        tempList = sys.stdin.readline().strip().split()
        name, kind = tempList
        graph[kind].add(name)

    answer = 1
    for g in graph:
        answer *= (len(graph[g]) + 1)
    print(answer -1)