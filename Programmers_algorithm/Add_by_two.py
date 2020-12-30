
numbers = [2,1,3,4,1]
answer = []

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        print(numbers[i]+numbers[j])
        answer.append(numbers[i]+numbers[j])

print(answer)
answer = sorted(answer)
print(answer)
answer = set(answer)
answer = list(answer)
sorted(answer)
print(answer)