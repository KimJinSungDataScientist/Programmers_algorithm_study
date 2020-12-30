n = 5
lost = [2, 4]
reserve= [1,3,5]


same = list(set(lost).intersection(reserve))

if same is not None:
    for i in range(len(same)):
        reserve.remove(same[i])
        lost.remove(same[i])

for i in reserve:
    if i - 1 in lost:
        lost.remove(i-1)
    elif i + 1 in lost:
        lost.remove(i+1)

print(n-len(lost))