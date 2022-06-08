from dis import dis
import heapq

# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C 입력받기
n, m, start = map(int, input().split())

# 도시별 거리 테이블 초기화
INF = 1e9
distance = [INF] * (n + 1)
# 도시별 방문 테이블 초기화
visited = [0] * (n + 1)

# 통로 및 걸리는 시간 입력받기
graph = [[] for _ in range (n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

# 다익스트라 알고리즘을 통해 start 도시부터 다른 도시까지의 최소거리 구하기
def solve():
    global distance, visited, graph
    queue = []
    # 시작지점 힙에 넣고 방문처리
    heapq.heappush(queue, (0, start))
    visited[start] = 1
    distance[start] = 0
    # 힙이 빌때까지 반복
    while(queue):
        tmp = heapq.heappop(queue)
        for v in graph[tmp[1]]:
            if visited[v[1]] == 0:
                heapq.heappush(queue, v)
                visited[v[1]] = 1
                distance[v[1]] = min(distance[v[1]], tmp[0] + v[0])

solve()
# 메시지를 받는 도시의 개수 찾기
# 가장 시간이 많이 걸리는 도시의 시간 구하기
count = 0
MAX = 0
for i in range(1, n + 1):
    if distance[i] != 0 and distance[i] != INF:
        count += 1
        MAX = max(MAX, distance[i])

# 출력
print(count, MAX)