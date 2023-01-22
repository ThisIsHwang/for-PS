from collections import deque
import heapq

def test_case_generator(n):
    import random
    name = ""
    for _ in range(n):
        name += random.sample(list("ABCD"), 1)[0]
    n = len(name)

    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    #return answer
    return name, answer


def solution(name):
    answer = 0
    name = list(name)
    currentName = ['A'] * len(name)
    now = 0

    queue = []
    visited = set()
    visited.add(0)
    heapq.heappush(queue, (answer, list(currentName), now, set(visited)))
    while True:
        answer, currentName, now, visited = heapq.heappop(queue)
        before = answer
        if name[now] != currentName[now]:
            answer += min(ord(name[now]) - ord('A'), ord('Z') - ord(name[now]) + 1)
            #answer += min(abs(ord(name[now]) - ord(currentName[now])), abs(ord(currentName[now]) - ord(name[now]) + 26))
            currentName[now] = name[now]

        if currentName == name:
            minAns = answer
            while queue:
                answer, currentName, now, visited = heapq.heappop(queue)
                if name[now] != currentName[now]:
                    tempAns = answer + min(ord(name[now]) - ord('A'), ord('Z') - ord(name[now]) + 1)
                    currentName[now] = name[now]
                    if currentName == name:
                        if tempAns < minAns:
                            minAns = tempAns
            answer = minAns
            break
        left = 1
        while True:
            if name[now - left] != currentName[now - left] and (len(currentName) + now - left) % len(currentName) not in visited:
                tempVisited = set(visited)
                tempVisited.add((len(currentName) + now - left) % len(currentName))
                heapq.heappush(queue, (answer + left , list(currentName), now - left, tempVisited))
                break
            left += 1
        right = 1
        while True:
            if name[now + right] != currentName[now + right] and (len(currentName) + now + right) % len(currentName) not in visited:
                tempVisited = set(visited)
                tempVisited.add((len(currentName) + now + right) % len(currentName))
                heapq.heappush(queue, (answer + right, list(currentName), now + right, tempVisited))
                break
            right += 1
    return answer

name = "AABD"
print(solution(name))
# real: 6
case, ans = test_case_generator(4)
while solution(case) == ans:
    case, ans = test_case_generator(4)
print(case, ans, solution(case))
#AABD 6 7

# 1 3 1 1

