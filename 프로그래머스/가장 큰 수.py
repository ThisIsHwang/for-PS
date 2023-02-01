
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = [n*3 for n in numbers]
    numbers.sort(reverse=True)

    return str(int("".join([n[:int(len(n)/3)] for n in numbers])))


numbers = [0,0,0,0]
print(solution(numbers))