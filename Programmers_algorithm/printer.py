def solution(priorities, location):
    answer = 0

    while priorities:
        for i in range(1, len(priorities)):
            if priorities[0] < priorities[i]:
                priorities.append(priorities[0])
                priorities.pop(0)
                if location == 0:
                    location = len(priorities)-1
                else:
                    location -= 1
                break
            if i == len(priorities) - 1:
                priorities.pop(0)
                answer += 1

                if location == 0:
                    return answer
                else:
                    location -= 1

            if len(priorities) == 1:
                return answer + 1

    return answer


print(solution(	[3,3,4,2],3))