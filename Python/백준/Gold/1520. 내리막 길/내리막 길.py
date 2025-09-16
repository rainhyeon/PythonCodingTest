# 오른쪽 아래로 이동하는 경로의 개수 구하기

import sys
sys.setrecursionlimit(10**6) # 깊이 높이기

Y, X = map(int, input().split()) # N: 행(y), M: 열(x)

graph = [list(map(int, input().split())) for _ in range(Y)]
answer = 0

def recur(y, x):
    
    if y == Y-1 and x == X-1:
        return 1 # 상하좌우로 뻗어나가다가, 맨 오른쪽 아래에 닿으면 1을 리턴하고
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    # 상, 하, 좌, 우
    for ex, ey in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
        nx, ny = x+ex, y+ey
    
        if 0 <= nx < X and 0 <= ny < Y:
            if graph[y][x] > graph[ny][nx]:
                # 1 값들을 전부 합친 게 (x,y)에서 출발해 도착까지 가는 총 경로 수
                route += recur(ny, nx) 

    dp[y][x] = route
    return dp[y][x]

dp = [[-1 for _ in range(X)] for _ in range(Y)]


answer = recur(0, 0)
print(answer)