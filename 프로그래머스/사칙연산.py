from collections import defaultdict
cache = defaultdict(int)

# 어떤 것을 dp할 것인가가 중요하다.
# 숫자 2개를 받고 operator를 받아서 cache에 dict 형태로 저장하자.
# 계산 시켜야되나?
# An+1 = max(An-1 + An, An-1 op An-2 + An)

# 두개씩 합쳐서 값을 합친다.
# 두개씩합쳐진 값을 저장한다.
# 3개씩 합쳐진 값을 더한다.(괄호까지 같이 저장해야될 듯)
#
def forDP(arr):
    global cache
    operator = ["+", "-"]
    #계속 결합하다가 길이가 1이면 정답을 반환한다.

    if len(arr) == 1:
        cache[tuple(arr)] = str(arr[-1])
    elif len(arr) == 0:
        cache[tuple(arr)] = " "

    if cache[tuple(arr)]:
        return cache[tuple(arr)]

    str1 = arr[:3]
    str2 = arr[:2]
    t1, t2 = 0, 0
    if cache[tuple(str1)]:
        t1 = cache[tuple(str1)]
    else:
        if str1[-1] in operator:
            t1 = str(eval("".join(str1[:-1])))
            t1 += str1[-1]
        else:
            t1 = str(eval("".join(str1)))
        cache[tuple(str1)] = t1

    if cache[tuple(str2)]:
        t2 = cache[tuple(str2)]
    else:
        if str2[-1] in operator:
            t2 = str(eval("".join(str2[:-1])))
            t2 += str(str2[-1])
        else:
            t2 = str(eval("".join(str2)))
        cache[tuple(str2)] = t2

    a = eval(t1 + forDP(arr[3:]))
    b = eval(t2 + forDP(arr[2:]))
    t = max(a, b)
    if t> 0:
        cache[tuple(arr)] = "+" + str(t)
    else:
        cache[tuple(arr)] = str(t)
    return cache[tuple(arr)]


def solution(arr):
    answer = -1
    answer = forDP(arr)
    return int(answer)


def solution2(arr):
    minmax = [0, 0]
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
    minmax[1] += sum_value
    return minmax[1]

arr = ['9', '-', '6', '-', '2', '+', '9']

print(solution(arr))
#print(solution(arr), solution2(arr))
n = 7
import random
while True:
    nums = [str(random.randint(1, 9)) for _ in range(n)]
    ops = [random.choice(["+", "-"]) for _ in range(n-2)]
    arr = []
    for i in range(n):
        if i % 2 == 0:
            arr.append(nums.pop(0))
        else:
            arr.append(ops.pop(0))


    if solution(arr) != solution2(arr):
        print(arr)
        print(solution(arr), solution2(arr))
        break


#print()

