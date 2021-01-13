s = "123456"


def solution(s):
    cnt = 0
    for i in s:
        if ord(i) >=65 and ord(i)<=122:
            cnt=0
            break
        cnt+=1

    if cnt == 4 or cnt == 6:
        return True
    else:
        return False


print(solution(s))