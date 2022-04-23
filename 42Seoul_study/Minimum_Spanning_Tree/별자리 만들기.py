import sys
from math import sqrt
input = sys.stdin.readline

# 부모 찾기 함수
def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

# 집합 연결 함수
def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 별의 개수 입력 받기
n = int(input())

# 별의 부모 테이블 선언 및 초기화
parents = [0] * (n + 1)
for i in range(1, n + 1):
    parents[i] = i

# 별의 위치와 별들 사이의 선을 담을 리스트 선언
stars = []
edges = []

# 별들을 리스트에 추가
for i in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

# 별들 사이의 선을 거리 계산하여 추가
for i in range(n):
    for j in range(i + 1, n):
        distance = sqrt((abs(stars[i][0] - stars[j][0])) ** 2 + (abs(stars[i][1] - stars[j][1])) ** 2)
        edges.append((distance, (i + 1), (j + 1)))

# 간선 비용순으로 오름차순 정렬
edges.sort()

result = 0
# 최소 스패닝 트리 찾기
for e in edges:
    if find_parent(parents, e[1]) != find_parent(parents, e[2]):
        union(parents, e[1], e[2])
        result += e[0]

print(result)