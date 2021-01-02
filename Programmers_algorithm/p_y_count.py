s = "PPPPyyyy"
s = s.lower()


def solution(s):
    cnt = 0

    for i in range(len(s)):
        if s[i]=='p':
           cnt+=1
        elif s[i]=='y':
            cnt-=1
    if cnt==0: return True
    else : return False

print(solution(s))