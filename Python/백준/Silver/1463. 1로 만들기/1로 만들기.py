# DP와 재귀로 풀기
# https://www.acmicpc.net/problem/1463

#n = int(input())
# dp = [-1 for _ in range(n+1)]

# def recur(x):

#     if x == 1:
#         return 0 # 1이면 연산횟수 0
    
#     if dp[x] != -1: # dp가 없데이트 되었다면 
#         return dp[x] # 그 값 출력
    
#     # 항상 가능한 연산 : -1
#     res = recur(x-1) + 1

#     if x % 2 == 0:
#         # x//2를 1로 만드는 최소 연산 횟수(recur(x//2))에 +1을 더한 게 “이번 경우의 연산 횟수
#         res = min(res, recur(x // 2) + 1)

#     if x % 3 == 0:
#         res = min(res, recur(x // 3) + 1)

#     dp[x] = res

#     return dp[x]

# print(recur(n))


#---------------------------------------------------
# 바텀업으로 풀기

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1]+1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
