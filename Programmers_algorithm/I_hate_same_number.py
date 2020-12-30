arr = [1,1,3,3,0,1,1]
answer = [arr[0]]

for i in range(1,len(arr)):
    if arr[i-1]!=arr[i]:
        answer.append(arr[i])

print(answer)


#v2
for i in arr:
    print(arr[-1:], [i])