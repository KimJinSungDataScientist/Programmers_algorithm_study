def solution(s):
    num = len(s)//2

    answer = list(s)
    save = []
    count_word = ""
    save_total = []

    for j in range(1,num+1):
        for i in range(len(s)//j+1):
            if answer[i*j:i*j+j]:
                save.append(answer[i*j:i*j+j])

        save_text = save.pop(0)
        cnt = 1

        while save:
            temp = save.pop(0)

            if save_text == temp:
                cnt += 1

                if not save:
                    count_word += str(cnt) + "".join(save_text)
                    cnt = 1

            else:
                if cnt != 1:
                    count_word += str(cnt) + "".join(save_text)
                    cnt = 1

                    if not save:
                        count_word += "".join(temp)

                else:
                    count_word +=  "".join(save_text)

                    if not save:
                        count_word += "".join(temp)

                save_text = temp

        if count_word:
            save_total.append(len(count_word))

        count_word = ""
    if len(s)==1:
        return 1

    return (min(save_total))

print(solution("a"))