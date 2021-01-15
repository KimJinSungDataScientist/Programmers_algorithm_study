def solution(n):
    return list(map(lambda x : int(x), reversed(list(str(n)))))


solution(12345)