
def random_case_generator(n):
    import random
    lost = random.sample(range(1, n), random.randint(0,n-1))
    reserve = random.sample(range(1, n), random.randint(0,n-1))
    arr = [1] * n
    for l in lost:
        arr[l - 1] -= 1
    for r in reserve:
        arr[r - 1] += 1

    for i in range(n - 1):
        if arr[i] == 0 and arr[i + 1] == 2:
            arr[i] = 1
            arr[i + 1] = 1
        if arr[i] == 2 and arr[i + 1] == 0:
            arr[i] = 1
            arr[i + 1] = 1
    answer = n - arr.count(0)
    return n, lost, reserve, answer




def solution(n, lost, reserve):
    answer = 0
    setlost = set(lost) - set(reserve)
    setreserve = set(reserve) - set(lost)

    for l in sorted(list(setlost)):
        if l - 1 in setreserve:
            setreserve.remove(l - 1)
            setlost.remove(l)
        elif l + 1 in setreserve:
            setreserve.remove(l + 1)
            setlost.remove(l)
    answer = n - len(setlost)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3]
print(solution(n, lost, reserve))

n = 5
n, lost, reserve, answer = random_case_generator(n)
while True:
    *par, answer = random_case_generator(n)
    if solution(*par) != answer:
        print(f"incorrect for case:{par}")
        break

print()