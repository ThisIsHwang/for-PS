import sys
from collections import defaultdict
n, k = map(int, input().split())
x = list(map(int, input().split()))
new = [list(map(int, input().split())) for _ in range(k)]
dap = [0]
for i in range(n):
    dap.append(dap[i] + x[i])
for t in range(k):
    print(dap[new[t][1]]-dap[new[t][0]-1])
