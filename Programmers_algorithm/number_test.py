def solution(n):
    answer = ''


    while n>3:
        if n%3!=0:
            answer = str(n%3) + answer
            n//=3
        else:
            answer = str((n//3) - 1) + answer
            n = n//3 - 1

    answer = str(n) + answer
    answer = answer.replace("3", "4")

    return answer

print(solution(10))