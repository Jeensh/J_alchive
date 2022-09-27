# 1 ~ n번까지의 헛간
# 술래는 항상 1번 헛간에서 시작
# 총 M개의 양방향 통로
# 1번 헛간으로부터 최단 거리가 가장 먼 헛간
# 최단 거리는 지나야 하는 길의 최소 개수를 말함
from dis import dis
import heapq

INF = int(1e9)

# n, m 입력받기
n, m = map(int, input().split())

# 서로 연결된 헛간 정보 입력받기
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for tmp in graph[now]:
        cost = dist + 1
        if cost < distance[tmp]:
            distance[tmp] = cost
            heapq.heappush(q, (cost, tmp))

MAX = -1
idx = -1
for i in range(1, n + 1):
    if MAX < distance[i]:
        MAX = distance[i]
        idx = i

count = 0
for i in range(idx, n + 1):
    if distance[i] == MAX:
        count += 1

print(idx, MAX, count)