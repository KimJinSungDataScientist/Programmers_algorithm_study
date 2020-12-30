answer = 0
save = []
n=50


while(n>=3):
    save.append(int(n%3))
    n = int(n/3)
save.append(n)



for i in range(len(save)):
    answer += (3**i)*save[-(i+1)]

print(answer)