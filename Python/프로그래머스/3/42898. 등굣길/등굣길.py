def solution(m, n, puddles): # m: x, n:y
        
    answer = 0
    
    dp = [[-1]*m for _ in range(n)]
    puddle_set = {(x-1, y-1) for x, y in puddles}
    
    def recur(y, x):
        if (x, y) in puddle_set:
            return 0
        
        if y == n-1 and x == m-1:
            return 1
        
        if dp[y][x] != -1:
            return dp[y][x]
        
        route = 0
        # 오른쪽과 아래(y,x) > [0,1], [1,0]
        for ey, ex in [[0,1], [1,0]]:
            dy, dx = y + ey, x + ex
            
            # 범위 내라면
            if 0 <= dy < n and 0 <= dx < m:
                route += recur(dy, dx)
                
        dp[y][x] = route % 1000000007
        return dp[y][x]
        
        
    answer = recur(0, 0) % 1000000007
    
    return answer