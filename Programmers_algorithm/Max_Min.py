# def solution(n, m):
#     answer = []
#     save = 1
#     cnt = m
#
#
#     for i in range(1,n+1):
#         if n%i == m%i == 0:
#             save = i
#     answer.append(save)
#
#     while True:
#         if cnt%n == cnt%m:
#             break
#         cnt+=1
#
#     answer.append(cnt)
#
#     return answer
#
# print(solution(100,123))


def solution(n,m):
    c,d = max(n,m),min(n,m)
    t=1
    while t > 0:
        t = c%d
        c, d = d, t # 유클리디안 호제법 : 작은수 : 몫, 나누는 수 : 나머지, 나머지가 0보다 클때동안 반복

    return [c,int(n*m/c)] # 최소공배수는 원래 값 두개 곱한다음, 최대공약수로 나눠주면 됨


print(solution(3,12))