N, K = map(int, input().split()) # N: 물품의 수, K: 버틸수있는 무게

obj = [list(map(int, input().split())) for _ in range(N)]

def recur(index, weight):
    global ans

    if weight > K: # 무게를 넘치면
            return -9999999

    if index == N: # 모든 물건을 넣었다면
        return 0
    

    # dp에 저장되어있는게 있다면, 저장된 값을 출력한다
    if dp[index][weight] != -1:
        return dp[index][weight]

    # 배낭에 넣는다면, 넣지 않는다면에서 최대
    dp[index][weight] = max(recur(index+1, weight+obj[index][0]) + obj[index][1], recur(index+1, weight))

    return dp[index][weight]
    
# dp를 2차원으로 만들어서 [넣은 물건의 개수][무게] -> 무게까지 고려해야하기때문에 2차원 배열
dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]
ans = recur(0, 0)
print(ans)