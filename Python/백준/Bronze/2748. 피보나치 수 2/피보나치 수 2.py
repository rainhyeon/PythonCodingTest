# https://www.acmicpc.net/problem/2748
# 피보나치 수 2

N = int(input())


def fibo(n):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo(n-1) + fibo(n-2)

    return dp[n]

dp = [-1 for _ in range(N+1)]
dp[0], dp[1] = 0, 1

answer = fibo(N)
print(answer)