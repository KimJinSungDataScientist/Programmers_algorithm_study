def balance(p):
    cnt1 = 0
    cnt2 = 0
    temp = []
    bae_u = []
    bae_v = []

    if not p:
        return ""

    for i in p:  # p에서 문자열 뽑아오다 균형 잡히면 바로 컽
        if i == '(':
            cnt1 += 1
        else:
            cnt2 += 1

        bae_u.append(i)

        if cnt1 != 0 and cnt1 == cnt2 and cnt1 + cnt2 != len(p):
            bae_v += p[cnt1 + cnt2:]
            break

    if u_balance(bae_u):
        if bae_v:
            bae_u += balance(bae_v)
        return bae_u

    else:
        temp.append('(')
        temp += balance(bae_v)
        temp.append(')')
        bae_u.pop(0)
        bae_u.pop(-1)
        for i in range(len(bae_u)):
            if bae_u[i] == '(':
                bae_u[i] = ')'
            else:
                bae_u[i] = '('

        temp += bae_u

    return temp


def u_balance(bae_u):  # u배열이 올바른지 판단
    cnt = 0

    for i in bae_u:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    return True


def solution(p):
    answer = balance(p)

    return "".join(answer)


print(solution("()))((()"))
