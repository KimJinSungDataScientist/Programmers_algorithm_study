def solution(s, n):
    s = list(map(lambda x: ord(x), s))

    for i in range(len(s)):
        if s[i]>=65 and s[i]<=90:
            s[i] = (s[i]+n)%91
            if s[i]<65:
                s[i] += 65

        elif s[i]>=97 and s[i]<=122:
            s[i] = (s[i] + n)%123
            if s[i]<97:
                s[i] += 97

    answer = (''.join(list(map(lambda x: chr(x), s))))

    return answer


print(solution("AB",1))