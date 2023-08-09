# 초기에 {0}, {1} ..{n} 이 각각 n + 1개의 집합을 이루고 있음
# 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다
# 집합을 표현하는 프로그램을 만들어라

# 유니온 함수
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 파인드 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

########## 진행 ##########
# n, m 입력받기
# m은 입력으로 주어지는 연산의 개수
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]

# 연산 입력받기
# o, a, b
# o :  -> 합집합, o : 1 -> 두 원소가 같은 집합에 포함되어 있는지 확인
for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(parent, a, b)
    elif o == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print('NO')