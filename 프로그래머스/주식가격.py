


def solution(prices):
    answer = []
    newPrices = prices[:-1]
    for i in range(len(prices) - 1):
        cnt = 0
        for ii in range(1, len(prices) - i):
            if prices[i] > prices[i + ii]:
                break
        cnt += ii
        # if cnt == 0:
        #     cnt = 1
        answer.append(cnt)
    answer.append(0)
    return answer


prices = [5, 8, 6, 2, 4, 1]
print(solution(prices))