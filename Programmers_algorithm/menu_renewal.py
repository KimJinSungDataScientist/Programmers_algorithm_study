from itertools import permutations
from itertools import combinations

def solution(orders, course):
    orders = list(map(lambda x: "".join(sorted(x)), orders))

    answer_temp = []
    answer = []

    for c in course:
        temp2 = {}
        for i in orders:
            if len(i) >= c:
                temp = list(combinations(i, c))
                for j in temp:
                    if j in temp2:
                        temp2[j] += 1
                    else:
                        temp2[j] = 1
        if temp2:
            key = max(temp2.values())

        if key<2:
            break

        for i in temp2:
            if temp2[i] == key:
                answer_temp.append(i)


    for i in answer_temp:
        answer.append("".join(i))

    return sorted(answer)


print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))