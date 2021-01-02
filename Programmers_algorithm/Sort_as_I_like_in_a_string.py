#strings = ['zzz','zad','sun', 'cerr','bedza','abc','aaa','zzzzz','zad','sun', 'cerr','bedzd','aeo','zad','sun', 'cerr','bedzd','bedz', 'bedzd', 'cer','caa', 'car']
strings = ['apple','banana','cat']
n = 1

answer = []

answer.append(strings[0])
strings.remove(strings[0])

for i in strings:
    for j in answer:
        if i[n] < j[n]:
            answer.insert(answer.index(j), i)
            break

        elif i[n] == j[n]:
            cnt = 0

            while answer[answer.index(j)+cnt]<i and answer[answer.index(j)+cnt][n]== i[n]:
                cnt+=1
                if answer.index(j)+cnt == len(answer):
                    break

            answer.insert(answer.index(j) + cnt, i)
            break

        elif j == answer[len(answer) - 1]:
            answer.append(i)
            break

print(answer)