def solution(tickets):
    answer = []
    n = len(tickets)
    
    visited = [False] * n
    
    def dfs(path, depth):
        if depth == len(tickets):
            answer.append(path)
            return
        
        for i in range(n):
            if not visited[i] and tickets[i][0] == path[-1]:
                visited[i] = True
                dfs(path + [tickets[i][1]], depth + 1)
                visited[i] = False # 백트레킹
                
    dfs(["ICN"], 0)
    return sorted(answer)[0] # 알파벳 순