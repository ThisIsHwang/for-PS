# 나머지와 수학 연산을 사용해야 한다.

# x : 3, y : 9
# M = 10, N = 12
# 1~10번째 = <1: 1> ~ <10:10>
# 11번째 ~ 12번째 = <1:11>, <2:12>
# 13번쨰 ~ 24번째 <3:1><4:2> ~ <4:12>



import sys

def getDays(M, N, x, y):
    while x <= M * N:
        if not((x - y) % N):
            return x
        x += M
    return -1



k = int(sys.stdin.readline().strip())
for _ in range(k):
    M, N, x, y = list(map(int, sys.stdin.readline().strip().split()))
    print(getDays(M, N, x, y))
#print()