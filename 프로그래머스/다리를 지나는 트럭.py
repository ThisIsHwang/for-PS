bridge_length = 3
weight = 5
truck_weights = [4]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    currentWeight = 0
    currentOnTruck = deque()

    time += 1

    while truck_weights:
        t = truck_weights.popleft()
        while True:
            if weight >= currentWeight + t and len(currentOnTruck) < bridge_length:
                currentWeight += t
                currentOnTruck.append((time + bridge_length, t))
                time += 1
                break
            else:

                outTime, newWeight = currentOnTruck.popleft()
                if time < outTime:
                    time = outTime
                currentWeight -= newWeight

    if currentOnTruck:
        time = currentOnTruck[-1][0]
    return time

print(solution(bridge_length, weight, truck_weights))