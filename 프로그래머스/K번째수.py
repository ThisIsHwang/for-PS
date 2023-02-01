def solution(array, commands):
    answer = []
    for i, j, k in commands:
        tempArray = array[i-1:j]
        tempArray = sortingIt(tempArray)
        answer.append(tempArray[k-1])
    return answer

def sortingIt(array):
    if len(array) == 1:
        return array

    a = sortingIt(array[:len(array)//2])
    b = sortingIt(array[len(array)// 2:])

    aIdx = 0
    bIdx = 0

    tempArray = list()
    while aIdx != len(a) and bIdx != len(b):
        if a[aIdx] < b[bIdx]:
            tempArray.append(a[aIdx])
            aIdx += 1
        else:
            tempArray.append(b[bIdx])
            bIdx += 1

    while aIdx < len(a):
        tempArray.append(a[aIdx])
        aIdx += 1

    while bIdx < len(b):
        tempArray.append(b[bIdx])
        bIdx += 1
    return tempArray


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))