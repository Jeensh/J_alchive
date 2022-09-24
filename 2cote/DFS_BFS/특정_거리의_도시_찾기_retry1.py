from collections import deque

# 도시의 개수 n
# 도로의 개수 m
# 거리 정보 k
# 출발 도시의 정보 x
n, m, k, x = map(int, input().split())

# 도로 정보
graph = [[] for i in range(n + 1)]

# 도로 정보 입력받기
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

# 각 도시의 최단 거리 테이블
result = [-1] * (n + 1)

# 각 도시를 BFS로 최단거리 갱신
q = deque([x])
result[x] = 0
while q:
    now = q.pop()
    if result[now] > k:
        break
    for i in graph[now]:
        q.appendleft(i)
        if result[i] == -1:
            result[i] = result[now] + 1

# 출력
check = True
for i in range(1, n + 1):
    if result[i] == k:
        print(i)
        check = False
if check:
    print(-1)