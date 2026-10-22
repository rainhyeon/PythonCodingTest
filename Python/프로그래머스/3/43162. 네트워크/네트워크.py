
def solution(n, computers):
    answer = 0
    
    # 일차원 배열로 가능
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for j in range (n):    
            if computers[node][j] == 1 and not visited[j]:
                dfs(j) # node를 중심으로 j를 진행하다가 j도 깊이 탐색함
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1 # 모든 방문이 끝났을때 +1
    
    return answer