import heapq

def dijkstra(graph, start, end):
    # distances: 각 노드까지의 최소 비용을 저장하는 딕셔너리. 처음에는 무한대로 초기화.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드까지의 거리는 0
    
    # 이전 노드 정보를 저장해 경로를 복원하는데 사용
    previous_nodes = {node: None for node in graph}
    
    # 우선순위 큐 (최소 힙): (비용, 노드)
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 현재 꺼낸 노드까지의 거리가 기존 최소 거리보다 크면 무시
        if current_distance > distances[current_node]:
            continue
        
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 발견하면 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                previous_nodes[adjacent] = current_node  # 이전 경로 저장
                heapq.heappush(queue, (distance, adjacent))
    
    # 경로 복원
    path = []
    current = end
    
    # previous_nodes를 거슬러 올라가면서 경로 추적
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    
    path.reverse()  # 거꾸로 되어 있으므로 뒤집기
    
    return distances[end], path  # 최소 비용과 경로 반환


# -----------------------
# 입력 처리
# 간선 수 입력
n = int(input("간선 개수를 입력하세요: "))

graph = {}

print("간선 정보를 입력하세요 (시작 도착 비용):")
for _ in range(n):
    a, b, cost = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = cost
    graph[b][a] = cost  # 무방향 그래프

# 시작 / 종료 노드 입력
start_node = int(input("출발 노드: "))
end_node = int(input("도착 노드: "))

# 다익스트라 실행
min_cost, shortest_path = dijkstra(graph, start_node, end_node)

# 결과 출력
print(f"최소 비용: {min_cost}")
print(f"경로: {' -> '.join(map(str, shortest_path))}")
