def solution(s):
    s = s.lower()

    s = s.split(" ")

    for i in range(len(s)):
        temp = list(s[i])
        for j in range(len(s[i])):
            if j%2==0:
                temp[j] = s[i][j].upper()
        s[i]="".join(temp)
    s = " ".join(s)

    return s


print(solution("Produce manufacture produce manufacture produce manufacture"))
