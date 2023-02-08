
#
# |--| |  |  |--|--|  | | |
#
# |  |  |  |  |

import sys

dp = [1, 1, 3] * 1001

n = int(sys.stdin.readline())

for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)
