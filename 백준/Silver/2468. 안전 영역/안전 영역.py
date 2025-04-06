import sys
sys.setrecursionlimit(100000)  # 충분히 늘리기
input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h, visited, graph, n):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > h:
                dfs(nx, ny, h, visited, graph, n)

def main():
    n = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(n)]

    max_height = max(max(row) for row in graph)
    result = 0

    for h in range(0, max_height + 1):  # 강수량
        visited = [[False] * n for _ in range(n)]
        safe_area = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and graph[i][j] > h:
                    dfs(i, j, h, visited, graph, n)
                    safe_area += 1
        result = max(result, safe_area)

    print(result)

if __name__ == "__main__":
    main()
