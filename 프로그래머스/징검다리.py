distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)


    low = 0
    high = distance

    while low <= high:
        prev = 0
        cnt = 0
        mid = (low + high) // 2
        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock

        if cnt > n:
            high = mid - 1
        else:
            answer = mid
            low = mid + 1

    return answer

print(solution(distance, rocks, n))