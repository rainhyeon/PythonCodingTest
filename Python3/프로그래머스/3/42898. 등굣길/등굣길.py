def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    
    water = set((y-1, x-1) for x, y in puddles)
    
    road = [[0] * m for _ in range(n)]
    
    road[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if (i,j) in water:
                road[i][j] = 0
                continue
            
            if i > 0:
                road[i][j] += road[i-1][j]
                
            if j > 0:
                road[i][j] += road[i][j-1]
                
            road[i][j] %= MOD
            
    return road[n-1][m-1]