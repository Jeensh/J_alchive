
INF = int(1e9)

# 도시의 개수 n 입력받기
n = int(input())

# 버스의 개수 m 입력받기
m = int(input())

# 거리 테이블 만들기
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 버스 정보 입력받기
for i in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘으로 거리 테이블 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in graph[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end = " ")
        else:
            print(j, end = " ")
    print()