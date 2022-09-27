# 출발지점에서 목표지점까지 최적의 경로를 찾기
# n x n 공간
# 0,0 에서 n-1, n-1로 이동하는 최소비용을 출력하기
import heapq

# 무한
INF = (1e9)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
# 테스트케이스 만큼 반복
for _ in range(int(input())):
    # n 입력받기
    n = int(input())

    costs = []
    # 각 칸의 비용을 입력받기
    for i in range(n):
        costs.append(list(map(int, input().split())))

    # 비용을 이용하여 그래프 만들기
    graph = [[] for i in range(n * n)]
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    # (길 번호, 비용)
                    graph[(x * n) + y].append((((nx * n) + ny), costs[nx][ny]))

    # 비용 테이블
    table = [INF] * (n * n)
    q = []
    heapq.heappush(q, (costs[0][0], 0))
    table[0] = costs[0][0]

    while q:
        c, now = heapq.heappop(q)
        if table[now] < c:
            continue
        for tmp in graph[now]:
            cost = c + tmp[1]
            if cost < table[tmp[0]]:
                table[tmp[0]] = cost
                heapq.heappush(q, (cost, tmp[0]))

    result.append(table[(n * n) - 1])

for i in result:
    print(i)