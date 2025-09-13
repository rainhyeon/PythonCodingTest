# 최대 이익을 출력해랴

N = int(input()) # 개수
works = [list(map(int, input().split())) for _ in range(N)]
#print(works)

def recur(index):
    global answer
    #print(f"{index}, {price}")

    if index == N: # 범위를 넘어가면(N부터)
        return 0
    if index > N:
        return -999999999
    
    # 계산되어있다면 
    if dp[index] != -1:
        return dp[index] # 계산된것을 가져와라

    # 상답을 받거나 안받거나 중에 더 max인것을 dp에 저장하겠다
    dp[index] = max(recur(index+works[index][0])+works[index][1], recur(index+1))
    
    return dp[index] # 중간에 계산했던걸 가져올 수 있도록 

dp = [-1 for _ in range(N+1)] # 1~시작하도록 하기위해서
recur(0)
print(dp[0])

