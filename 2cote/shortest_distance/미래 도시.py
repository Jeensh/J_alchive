# 회사 수 N과 경로의 개수 M입력받기
from random import randrange


n, m = map(int, input().split())

# 회사간 경로 입력받아 그래프 만들기
INF = (10e9)
graph = [[10e9 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
# 자기자신에게 가는 비용 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 도착지점과 중간지점 입력받기
end, mid = map(int, input().split())

# 선택 노드
for i in range(1, n + 1):
    # 출발 노드
    for j in range(1, n + 1):
        # 도착 노드
        for k in range(1, n + 1):
            # 출발지점이나 도착지점 중 지금 선택한 노드가 있으면 스킵
            if j == i or k == i:
                continue
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 출력
result = graph[1][mid] + graph[mid][end]
if result >= (10e9):
    print(-1)
else:
    print(result)