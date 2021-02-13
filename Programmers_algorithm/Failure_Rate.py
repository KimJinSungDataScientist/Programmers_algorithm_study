def solution(N, stages):
    save = {}
    answer = []
    total = len(stages)

    for i in range(0,N):
        if total == 0:
            save[i + 1] = 0
            continue

        save[i+1] = (stages.count(i+1)/total)
        total -= stages.count(i+1)

    save = sorted(save.items(),key=lambda x:x[1],reverse=True)

    for i in save:
        answer.append(i[0])

    return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))