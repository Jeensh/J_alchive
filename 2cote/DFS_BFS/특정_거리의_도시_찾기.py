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
result = [10 ** 6] * (n + 1)

# 출발 도시부터 출발하여 진입 레벨이 k가 되면 중지
def solve(v, level, k, result):
    # 도착한 곳 최단거리 갱신
    result[v] = min(result[v], level)

    # 진입 레벨이 k가 되면 중지
    if level >= k:
        return

    for i in graph[v]:
        solve(i, level + 1, k, result)


solve(x, 0, k, result)
# 도착한 곳이 있는지 체크하는 플래그
flag = False
for i in range(1, len(result)):
    if result[i] == k:
        flag = True
        print(i)
if not flag:
    print(-1)