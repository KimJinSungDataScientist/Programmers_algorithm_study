def solution(dartResult):
    save = []

    for i in range(len(dartResult)):
        if dartResult[i].isdigit() == True:
            cnt = int(dartResult[i])

            if dartResult[i+1] == '0':
                cnt = 10
                i+=1

            if dartResult[i+1]=='S':
                save.append(cnt)
            elif dartResult[i+1]=='D':
                save.append(cnt**2)
            elif dartResult[i+1]=='T':
                save.append(cnt**3)

        elif dartResult[i] == '*':
            try:
                save[-2] *= 2
                save[-1] *= 2
            except IndexError:
                save[-1] *= 2

        elif dartResult[i] == '#':
                save[-1] *= -1

    return sum(save)



print(solution('1D2S#10S'))