# dp
# 같은 숫자를 사더라도 최대한 비싸게.

# 1개 살때 비싸게, 2개 살때 비싸게
# 각 개수별로 최대로 비싼걸 찾자.
import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * (n + 1)


dp[0] = 0
dp[1] = p[0]

for i in range(1, n):
    for ii in range(i+1):
        dp[i + 1] = max(dp[i + 1], dp[ii] + p[i -ii])
print(dp[n])
