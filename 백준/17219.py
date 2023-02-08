
#메모장 사이트 주소, 비밀번호 저장
# 눈으로 주소와 비밀번호 찾음

import sys

N, M = map(int, sys.stdin.readline().strip().split())
hash_dict = dict()

for _ in range(N):
    key, value = sys.stdin.readline().strip().split()
    hash_dict[key] = value

for _ in range(M):
    key = sys.stdin.readline().strip()
    print(hash_dict[key])