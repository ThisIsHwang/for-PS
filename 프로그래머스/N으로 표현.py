N = 5
number = 12

cache = dict()
#giho = set()

def solution(N, number):
    answer = -1
    if N == number:
        return 1
    cache[1] = {N}
    for i in range(2, 9):
        cache[i] = set()
        cache[i].add(int(str(N) * i))
        for j in range(1, i):
            for a in cache[j]:
                for b in cache[i - j]:
                    cache[i].add(a + b)
                    cache[i].add(a - b)
                    cache[i].add(a * b)
                    if b != 0:
                        cache[i].add(a // b)
        if number in cache[i]:
            answer = i
            break

    return answer

print(solution(N, number))
#assert solution(N, number) == 4, "정답이 아닙니다."