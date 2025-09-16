import sys
sys.setrecursionlimit(10**6)

# 최대한 많은 칸 이동하기

N = int(input()) # 정사각형 크기

graph = [list(map(int, input().split())) for _ in range(N)] # 사각형 내부

def recur(x, y):
    # dp에 값이 들어있다면 그 값을 출력해라
    if dp[x][y] != 0:
        return dp[x][y]
    # 4방향 이동(상, 하 좌, 우)
    for ex, ey in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        nx, ny = x+ex, y+ey
        #print(f"상하좌우: {nx}, {ny}")
        if 0 <= nx < N and 0 <= ny < N:
            if graph[x][y] < graph[nx][ny]: # 이동할 값이 큰 경우
                #print(f"들어와서 {x}, {y}")
                dp[x][y] = max(dp[x][y], recur(nx, ny) + 1)

    return dp[x][y]

dp = [[0 for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        recur(x, y)

# 행들중에서 최대값 찾고 그중에서 또 최대값 찾아서 +1
print(max(map(max, dp)) + 1)
