import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# union
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

# find
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 집의 개수 N, 길의 개수 M 입력받기
n, m = map(int, input().split())

# 부모 리스트 초기화
parent = [i for i in range(n + 1)]

# 길 목록 초기화
routes = []

# 길의 개수만큼 길의 정보 입력받기
for i in range(m):
    n1, n2, cost = map(int, input().split())
    routes.append((cost, n1, n2))

# 길 목록 오름차순 정렬
routes.sort()

# 최소 비용 신장트리에서 가장 비용이 큰 간선
max = routes[0][0]

# 최소 비용 신장 트리를 찾아 비용합 구하기
result = 0
for r in routes:
    if find(parent, r[1]) != find(parent, r[2]):
        print(r)
        union(parent, r[1], r[2])
        result += r[0]
        if max < r[0]:
            max = r[0]

print(result - max)