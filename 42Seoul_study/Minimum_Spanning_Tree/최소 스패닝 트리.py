import sys
input = sys.stdin.readline

# 정점의 부모 찾기 함수
def find_parent(parents, v):
    if v != parents[v]:
        parents[v] = find_parent(parents, parents[v])
    return parents[v]

# 두 집합(트리) 연결 함수
def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 정점, 간선 개수 입력 받기
V, E = map(int, input().split())

# 부모 테이블 초기화
parents = [0] * (V + 1)

# 간선을 담을 리스트 초기화
edges = []

# 부모 테이블을 자기 자신으로 초기화
for i in range(1, V + 1):
    parents[i] = i

# 모든 간선에 대한 정보를 입력 받기
for i in range(E):
    a, b, c = map(int, input().split())
    # 비용순으로 정렬하기 위해 c를 첫 번쨰 원소로 둠
    edges.append((c, a, b))

# 간선을 비용순으로 오름차순으로 정렬
edges.sort()

result = 0
# 비용이 작은 간선부터 사이클이 만들어지지 않는 간선들만 포함하여 비용 계산
for e in edges:
    c, a, b = e
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        result += c

print(result)