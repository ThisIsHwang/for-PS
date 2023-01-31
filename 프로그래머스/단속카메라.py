routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda x : x[1])
    before = -300001
    for r in routes:
        if r[0] > before:
            before = r[1]
            answer += 1

    return answer

print(solution(routes))