def solution(arr):
    if len(arr) == 1:
        return [-1]

    arr2 = arr[:]
    arr.sort()
    arr2.remove(arr[0])

    return arr2

print(solution([4,3,2,1]))