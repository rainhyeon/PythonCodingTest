import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 행렬, 시도횟수

graph = [list(map(int, input().split())) for _ in range(N)]


#print(graph)
#print(try_point)

prefix = [[0 for _ in range(N+1)] for _ in range(N+1)] # 2차원 배열

for y in range(N): # 행
    for x in range(N): # 열
        prefix[y+1][x+1] = prefix[y+1][x] + prefix[y][x+1] + graph[y][x] - prefix[y][x]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split()) # x=행, y=열
    answer = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

    print(answer)

