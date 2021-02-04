def solution(n):
    save = []
    answer = 0
    cnt=1

    while n > 0:
        save.append(int(n%10))
        n//=10
        save.sort(reverse=True)

    for i in range(1,len(save)+1):
        answer += (save[-i]*cnt)
        cnt *= 10

    print(answer)


solution(118372)