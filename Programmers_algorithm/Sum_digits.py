def solution(n):
    answer = 0

    n = list(str(n))
    for i in range(len(n)):
        answer+=int(n[i])
    return answer

print(solution(987))