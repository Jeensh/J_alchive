# n명인 학교에 입학
# 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다
# 준석이게에게는 총 k원의 돈이 있고, 그 돈을 이용해서 친구를 사귀기로 한다
# 친구의 친구는 친구다
# 가장 적은 비용으로 모든 사람과 친구가 되는 방법

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
# n, m, k 입력받기
n, m, k = map(int, input().split())

# 각 학생이 원하는 친구비
cost = list(map(int, input().split()))
cost.insert(0, 0)

# 부모 테이블
parent = [i for i in range(n + 1)]

# v, w 학생은 친구다
for i in range(m):
    v, w = map(int, input().split())
    union(parent, v, w)

# 간선 만들기
data = []
for i in range(1, n + 1):
    c = cost[i]
    data.append((c, i))

data.sort()
std = data[0][1]
result = cost[std]
for fee, a in data[1:]:
    if find(parent, std) != find(parent, a):
        union(parent, std, a)
        result += fee

if result > k:
    print('Oh no')
else:
    print(result)