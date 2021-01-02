arr = [3,2,6]
divisor = 10

answer = []

for i in arr:
    if i%divisor == 0:
        answer.append(i)

if not answer:
    answer.append(-1)

answer.sort()

print(answer)

