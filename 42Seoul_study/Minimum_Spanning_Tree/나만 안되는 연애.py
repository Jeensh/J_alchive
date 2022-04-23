import sys
input = sys.stdin.readline

# 부모 찾기 함수
def find_parent(parents, a):
    if a != parents[a]:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

# 집합 합치기 함수
def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 학교의 개수 N과 도로의 개수 M 입력받기
N, M = map(int, input().split())

# 남초/여초 정보
attribute = [0]
attribute  += list(input().split())

# 도로 받아올 리스트 선언
roads = []

# 도로 받아오기
for i in range(M):
    u, v, d = map(int, input().split())
    roads.append((d, u, v))

# 도로 비용 기준 오름차순으로 정렬
roads.sort()

# 부모 테이블 선언 및 초기화
parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i

# 최소 비용 변수 선언
result = 0
# 연결된 간선 개수 카운트 변수 선언
count = 0

# 최소 비용 경로 찾기
for r in roads:
    if find_parent(parents, r[1]) != find_parent(parents, r[2]):
        if attribute[r[1]] != attribute[r[2]]:
            count += 1
            union(parents, r[1], r[2])
            result += r[0]

if count != N - 1:
    print(-1)
else:
    print(result)