def solution(number, k):

    total = len(number) - k
    cnt = 0
    cnt2 = -1
    answer = number[0]
    number = number[1:]

    while True:
        cnt2+=1
        if cnt2 >= len(number):
            return answer
        if answer[-1]<=number[cnt2]:
            while answer and answer[-1]<number[cnt2] and cnt!=k:
                answer = answer[:-1]
                cnt += 1

            if len(answer) < total:
                answer+=number[cnt2]

            if cnt == k:
                answer += number[cnt2+1:]
                return answer
        else:
            if len(answer) < total:
                answer+=number[cnt2]

    return answer


print(solution("999991",3))