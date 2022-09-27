# 1~N 여행지
# 두 여행지를 연결하는 도로가 존재할 수 있음
# 여행 계획이 실행 가능한지 여부 확인
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 유니온 함수
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지 수 n, 여행 계획에 포함된 도시의 수 m
n, m = map(int, input().split())

# 여행지 정보 입력받기
graph = [[0] * (n + 1)]
for i in range(n):
    tmp = [0]
    graph.append(tmp + list(map(int, input().split())))

# 여행 계획 입력받기
plan = list(map(int, input().split()))

# 부모 테이블 초기화 후 그래프에 따라 부모 테이블 갱신
parent = [i for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            union(parent, i, j)

# 여행계획의 도시들이 모두 같은 서로소 집합에 있는지 확인
flag = False
group = find_parent(parent, plan[0])
for city in plan[1:]:
    if find_parent(parent, city) != group:
        flag = True
        break
if flag:
    print("NO")
else:
    print("YES")
