# G개의 탑승구 1 ~ G
# P개의 비행기
import sys
input = sys.stdin.readline

# find
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# G 입력받기
g = int(input())

# P 입력받기
p = int(input())

# 도킹할 수 있는 탑승구의 정보 입력받기
parent = [i for i in range(g + 1)]
count = 0

n_list = []
for i in range(p):
    n_list.append(int(input()))

for i in range(p):
    tmp = n_list[i]
    if find(parent, tmp) == 0:
        break
    union(parent, tmp, parent[tmp] - 1)
    count += 1

print(count)
