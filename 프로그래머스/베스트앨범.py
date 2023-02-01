from collections import OrderedDict
def func(data):
    keys = list(data.keys())
    return keys[0]

def solution(genres, plays):
    answer = []
    hash = OrderedDict()
    genresTotal = OrderedDict()
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in genresTotal:
            genresTotal[g] += p
        else:
            genresTotal[g] = p

        if g in hash:
            hash[g].append({p: i})
        else:
            hash[g] = list()
            hash[g].append({p: i})

    g = list(genresTotal.items())
    g.sort(reverse=True, key= lambda x : x[1])
    genresTotal = OrderedDict({k: v for k, v in g})
    for h in hash.keys():
        myKeys = hash[h]
        myKeys.sort(reverse=True,key=func)

    for g in genresTotal.keys():
        try:
            for i in range(2):
                answer.append(list(hash[g].pop(0).values())[0])
        except Exception:
            continue

    return answer

genres =["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
plays = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(solution(genres, plays))