# DP로 풀기

T = int(input())

# n은 문제에서 최대 11
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
    # 1더하기전, 2더하기전, 3더하기 전
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])
