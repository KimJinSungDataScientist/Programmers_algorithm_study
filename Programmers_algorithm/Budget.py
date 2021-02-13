def solution(d, budget):
    d.sort()
    save = 0
    answer = 0

    for i in range(len(d)):
        if budget<save+d[i]:
            break
        save+=d[i]
        answer+=1

    return answer


print(solution([1,3,2,5,4],9))