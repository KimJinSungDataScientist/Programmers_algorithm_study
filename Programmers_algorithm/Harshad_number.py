def solution(x):
    save = 0
    save2 = x

    while x!=0:
        save += (x%10)
        x = int(x/10)

    if save2%save==0:
        return True
    else:
        return False

solution(10)