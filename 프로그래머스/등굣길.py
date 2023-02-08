def solution(m, n, puddles):
    cache = [[-1] * (m + 1) for _ in range(n+1)]
    for i in range(len(cache)):
        cache[i][0] = 0
    for i in range(len(cache[0])):
        cache[0][i] = 0
    for puddle in puddles:
        cache[puddle[1]][puddle[0]] = 0
    cache[1][1] = 1
    for i in range(1, len(cache)):
        for ii in range(1, len(cache[0])):
            if i == 1 and ii == 1:
                continue
            if cache[i][ii]:
                cache[i][ii] = cache[i-1][ii] + cache[i][ii - 1]


    return cache[n][m]%1000000007


def solution2(m, n, puddles):
    # 행열 만들기
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for puddle in puddles:
        dp[puddle[1]][puddle[0]]=0

    check=False # 1행, 1열 도중에 puddle이 있는지 확인을 위해
    # 도중에 puddle이 없는한 1로 처리
    for i in range(1,n+1):
        if dp[i][1]==0: check=True

        if check: dp[i][1]=0
        else: dp[i][1]=1

    check=False # 1행, 1열 도중에 puddle이 있는지 확인을 위해
    # 도중에 puddle이 없는한 1로 처리
    for i in range(1,m+1):
        if dp[1][i]==0: check=True

        if check: dp[1][i]=0
        else: dp[1][i]=1

    # 2행 2열부터 왼쪽과 위에 해당하는 값을 더하여 최신화 진행
    for i in range(2,n+1):
        for j in range(2,m+1):
            if dp[i][j]==0: continue
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]%1000000007

import random

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
print(solution2(m, n, puddles))
while True:
    m = random.randint(0, 5)
    n = random.randint(0, 5)
    i = random.randint(0, m * n)
    puddles = [[random.randint(1, m), random.randint(1, n)] for _ in range(i)]
    try:
        if solution(m, n, puddles) != solution2(m, n, puddles):
            print(m, n)
            print(puddles)
    except:
        print(m, n)
        print(puddles)
#print(solution(m, n, puddles))