import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, visited, graph, n, m):
    visited[y][x] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(nx, ny, visited, graph, n, m)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    result = []

    while True:
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        if n == 0 and m == 0:
            break

        graph = []
        for _ in range(m):
            graph.append(list(map(int, data[idx:idx + n])))
            idx += n

        visited = [[False] * n for _ in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and graph[i][j] == 1:
                    dfs(j, i, visited, graph, n, m)
                    answer += 1

        result.append(answer)

    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()
