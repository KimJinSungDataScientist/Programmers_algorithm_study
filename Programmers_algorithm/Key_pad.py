def solution(numbers, hand):
    answer = ''
    pos_r = 12
    pos_l = 10

    for i in numbers:
        if i==0:
            i=11

        if i == 1 or i==4 or i==7:
            answer+="L"
            pos_l = i

        elif i==3 or i==6 or i==9:
            answer+="R"
            pos_r = i

        else:
            save_l = Find_len(pos_l,i)
            save_r = Find_len(pos_r,i)

            if save_l == save_r:
                if hand=="right":
                    pos_r = i
                    answer+='R'
                else:
                    pos_l = i
                    answer+='L'
            elif save_l > save_r:
                pos_r = i
                answer+='R'
            else:
                pos_l = i
                answer+='L'

    return answer

def Find_len(n,n2):
    Max = max(n,n2)
    Min = min(n,n2)
    cnt = 0

    if Max - Min == 3 or Max - Min == 1:
        return 1
    else:
        while Max!=Min:
            Max = max(Max, Min)
            Min = min(Max, Min)

            if Max-3 >=Min:
                Max-=3
            else:
                Max-=1
            cnt+=1
    return cnt

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))