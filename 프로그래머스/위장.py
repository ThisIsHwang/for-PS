def solution(clothes):
    hash = dict()
    for c, c2 in clothes:
        if c2 in hash:
            hash[c2].add(c)
        else:
            hash[c2] = set()
            hash[c2].add(c)
    answer = 1
    for h in hash.values():
        answer *= (len(h) + 1)
    answer -= 1
    return answer

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
