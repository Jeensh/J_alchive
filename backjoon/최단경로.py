import heapq
# 방향 그래프가 주어지면, 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성
# 모든 간선의 가중치는 10 이하의 자연수
# 모든 정점에는 1부터 v까지 번호가 매겨져 있음

INF = int(1e9)

# 시작점에 연결된 모든 간선을 큐에 넣는다
# 큐에서 가장 가중치가 낮은 간선을 뺸다
# 원래 distance와 이번 간선을 통해서 도착한 것 중에 더 작은 것을 distance로 갱신한다
# 도착한 정점과 연결된 모든 간선을 큐에 넣는다
# 단 이미 방문했던 곳은 제외한다
def dijk(graph, distance, start, v):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for item in graph[now]:
            w, k = item
            cost = dist + w
            if cost < distance[k]:
                distance[k] = cost
                heapq.heappush(q, (cost, k))


########### 진행 ###########
# 정점의 개수 v, 간선의 개수 e 입력받기
v, e = map(int, input().split())


# 시작 정점의 번호
start = int(input()) - 1

# 각 간선 입력받기
# u, v, w : u에서 v로 가는 가중치 w인 간선이 존재
distance = [INF] * v
graph = [[] for _ in range(v)]
for i in range(e):
    u, k, w = map(int, input().split())
    u -= 1
    k -= 1
    graph[u].append((w, k))

dijk(graph, distance, start, v)
for d in distance:
    if d == INF:
        print('INF')
    else:
        print(d)
