
answers = [1,3,2,4,2]

N1_p = [1,2,3,4,5]
N2_p = [2,1,2,3,2,4,2,5]
N3_p = [3,3,1,1,2,2,4,4,5,5]
N1_s = 0
N2_s = 0
N3_s = 0

for i in range(len(answers)):

    if N1_p[i%5] == answers[i]:
        N1_s += 1
    if N2_p[i%8] == answers[i]:
        N2_s += 1
    if N3_p[i%10] == answers[i]:
        N3_s += 1

save = {1:N1_s , 2 : N2_s, 3:N3_s}
answer = []

for i in save:
    if max(save.values()) == save[i]:
        answer.append(i)

print(answer)
