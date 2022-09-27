# N개의 집과 M개의 도로
# 0 ~ n-1 번
# 가로등을 하루동안 켜는 비용 = 해당 도로의 길이
# 일부 가로등 비활성화, 마을에 있는 임의의 두 집의 가로등이 켜진 도로만 오갈 수 있음
# 일부 가로등을 비활성화 하여 최대한 많은 금액을 절약하고자 함
# 절약할 수 있는 최대 금액 정하기

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n, m 입력받기
n, m = map(int, input().split())

# 도로 정보 입력받기
# x, y, z : x번과 y번 사이의 집 거리 = z
roads = []
for i in range(m):
    x, y, z = map(int, input().split())
    roads.append((z, (x, y)))

# 비활성화 전 전체 비용 구하기
total = 0
for r in roads:
    total += r[0]

# 부모 테이블 초기화
parent = [i for i in range(n)]

# 최소비용 신장트리 구하기
# 간선 오름차순 정렬
roads.sort()
save = 0
for r in roads:
    cost = r[0]
    x, y = r[1]
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        save += cost
print(total - save)