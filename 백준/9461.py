import sys

tc = int(sys.stdin.readline())

p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(3, len(p)):
    p[i] = p[i-2] + p[i-3]

for _ in range(tc):
    print(p[int(sys.stdin.readline())])
