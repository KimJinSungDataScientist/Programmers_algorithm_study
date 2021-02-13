def solution(n, arr1, arr2):
    answer = []


    for i in range(n):
        save = []
        save_num = arr1[i]
        save_num2 = arr2[i]
        for j in range(n):
            if (save_num%2 or save_num2%2) == 0:
                save.insert(0," ")
            else:
                save.insert(0,"#")
            save_num //= 2
            save_num2 //= 2
        answer.append("".join(save))

    return answer



n=5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]

print(solution(n,arr1,arr2))