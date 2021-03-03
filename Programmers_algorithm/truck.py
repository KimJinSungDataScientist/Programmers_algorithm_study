def solution(bridge_length, weight, truck_weights):
    loading = [0] * len(truck_weights)
    end_truck = []
    on_truck = []

    on_truck.append(truck_weights.pop(0))

    cnt = 1
    cnt2 = 0
    time = 1
    sum_on_truck = on_truck[0]

    while on_truck:

        for i in range(cnt2, cnt):
            loading[i] += 1

            if loading[i] == bridge_length:
                cnt2+=1
                sum_on_truck -= on_truck[0]
                end_truck.append(on_truck.pop(0))

        if truck_weights:
            if weight >= truck_weights[0] + sum_on_truck:
                sum_on_truck += truck_weights[0]
                on_truck.append(truck_weights.pop(0))
                cnt += 1
        time += 1

    return time

print(solution(2,10,[7,4,5,6]))

