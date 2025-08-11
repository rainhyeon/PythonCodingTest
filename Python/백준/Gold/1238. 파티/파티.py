import sys
import heapq # 최소 힙(min-heap): 가장 작은 값이 항상 맨 앞(루트)에 오도록 하는 자료구조.

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)] # 1~N까지의 마을
reverse_graph = [[] for _ in range(N+1)]

def dijkstra(start, graph, n):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)] # (거리, 다음 위치)

    while pq:
        cur_dist, now = heapq.heappop(pq)
        if cur_dist > dist[now]: # 최소 거리가 다음 거리보다 클때
            continue
        for nxt, cost in graph[now]: # 현재노드(now)에서 갈 수 있는 다음 노드(nxt)와 해당 간선 비용(cost) 탐색 
            new_dist = cur_dist + cost # 새로운 거리 = 현재까지거리 + 이동 비용
            if new_dist < dist[nxt]: # 새로운 거리(new_dist)가 기존거리(dist[nxt])보다 작으면 -> 더 짧은 거리 찾음
                dist[nxt] = new_dist # 새롭게 갱신
                heapq.heappush(pq, (new_dist, nxt)) # new_dist가 제일 짧은 것을 먼저 꺼낸다
        
    return dist # 



for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t)) # a -> b 걸리는 시간: t
    reverse_graph[b].append((a, t)) # b -> a 걸리는 시간: t

dist_from_x = dijkstra(X, graph, N)
dist_to_x = dijkstra(X, reverse_graph, N)

max_time = 0
for i in range(1, N+1):
    round_trip = dist_to_x[i] + dist_from_x[i]
    max_time = max(max_time, round_trip)

print(max_time)
