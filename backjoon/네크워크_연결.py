import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
# 모든 컴퓨터가 연결이 되어있어야 함
# a와 b가 연결이 되어 있다는 말은, a에서 b로의 경로의 존재한다는 것을 의미
# a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면
# a, c는 연결이 되어 있다

# 그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하고 싶음
# 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때, 모든 컴퓨터를 연결하는 최소비용은?

# find 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union 함수
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

########### 진행 ###########
# n 입력받기
n = int(input())

# 연결할 수 있는 선의 수 m입력받기
m = int(input())

# 간선 입력받기
data = []
for i in range(m):
    a, b, c = map(int, input().split())
    data.append((c, a, b))

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]

data.sort()
result = 0
for c, a, b in data:
    if find(parent, a) != find(parent, b):
        result += c
        union(parent, a, b)
print(result)