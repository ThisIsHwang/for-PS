def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    hash = dict()
    hash["isLast"] = False
    for p in phone_book:
        tHash = hash
        if answer:
            for i in range(len(p)):

                if p[i] not in tHash:
                    tHash[p[i]] = dict()
                    tHash["isLast"] = False

                if tHash["isLast"] == True:
                    answer = False
                    break
                if i == len(p) - 1:
                    tHash["isLast"] = True
                    break
                tHash = tHash[p[i]]

        else:
            break
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))