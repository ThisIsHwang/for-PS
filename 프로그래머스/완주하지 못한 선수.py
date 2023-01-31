def solution(participant, completion):
    answer = ''
    participants = dict()
    for p in participant:
        if p in participants:
            participants[p] += 1
        else:
            participants[p] = 1

    answer = set(participants)
    for c in completion:
        if participants.get(c):
            participants[c] -= 1
            if participants[c] == 0:
                answer.remove(c)

    return answer.pop()

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))