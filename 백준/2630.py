import sys


colorPaper = list()
isVisited = list()

n = int(sys.stdin.readline().strip())
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    colorPaper.append(l)
    isVisited.append([False for _ in range(len(l))])

whiteCnt = 0
blueCnt = 0


def func1(partOfColorPaper, n):
    if n == 0:
        return

    isBlue = True
    isWhite = True
    global blueCnt
    global whiteCnt

    for i in range(n):
        #for ii in range(n):
            if isBlue or isWhite:
                for ii in range(n):
                    if partOfColorPaper[i][ii] != 1:
                        isBlue = False
                        #break
                    elif partOfColorPaper[i][ii] != 0:
                        isWhite = False
                        #break

    if isBlue:
        blueCnt += 1
    if isWhite:
        whiteCnt += 1
    if isWhite or isBlue:
        return

    c1 = [partOfColorPaper[i][:n // 2] for i in range(0, n//2)]
    c2 = [partOfColorPaper[i][:n // 2] for i in range(n // 2, n)]
    c3 = [partOfColorPaper[i][n // 2:] for i in range(0, n // 2)]
    c4 = [partOfColorPaper[i][n // 2:] for i in range(n // 2, n)]


    func1(c1, n // 2)
    func1(c2, n // 2)
    func1(c3, n // 2)
    func1(c4, n // 2)

func1(colorPaper, n)
print(whiteCnt)
print(blueCnt)
