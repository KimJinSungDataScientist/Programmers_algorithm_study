def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt != 0:
            answer.append(cnt)

    return answer

print(solution([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))