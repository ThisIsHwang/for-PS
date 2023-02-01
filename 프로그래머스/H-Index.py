def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    citations.append(0)
    for i in range(len(citations)):
        if i + 1 >= citations[i]:
            answer = citations[i]
            for c in range(citations[i] + 1, citations[i-1]):
                if i >= c:
                    answer = c
            break
    return answer

citations = [1, 1, 5, 7, 6]
print(solution(citations))
