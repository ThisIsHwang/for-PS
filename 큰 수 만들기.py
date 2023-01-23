def solution(number, k):
    answer = number[:]

    index = 0
    while index != len(answer)-1 and k != 0 :
        if int(answer[index]) < int(answer[index+1]):
            answer = answer[:index]+answer[index+1:]
            if index != 0 : index -= 1
            k -= 1
        else :
            index += 1
    if k != 0 :
        answer = answer[:len(answer)-k]

    return answer

number = "1231234"
k = 3

print(solution(number, k))

