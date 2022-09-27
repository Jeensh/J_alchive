# n개의 행성
# 행성을 연결하는 터널을 만들려고 함
# 행성은 3차원 좌표위의 한 점
# 터널을 총 N - 1개 건설해서 모든 행성이 연결되게 하려고함
# 모든 행성을 구하는데 필요한 최소비용

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 두 행성 a, b를 연결하는데 드는 비용 계산
def t_cost(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

# 조합 함수
def comb(arr, x):
    result = []

    if len(arr) < x:
        return result

    if x == 1:
        for i in arr:
            result.append([i])
    elif x > 1:
        for i in range(len(arr) - (x - 1)):
            for j in comb(arr[i + 1:], x - 1):
                result.append([arr[i]] + j)
    return result

# n 입력받기
n = int(input())

# 각 행성 정보 입력받기
# ((x, y, z), 행성 번호)
planets = []
for i in range(n):
    a, b, c = map(int, input().split())
    planets.append((a, b, c))

# 부모 테이블 초기화
parent = [i for i in range(n)]

# 간선 구하기
x_planets = []
y_planets = []
z_planets = []
for i in range(len(planets)):
    x_planets.append((planets[i][0], i))
    y_planets.append((planets[i][1], i))
    z_planets.append((planets[i][2], i))
x_planets.sort()
y_planets.sort()
z_planets.sort()

tunnels = []
for i in range(n - 1):
    tunnels.append((x_planets[i][1], x_planets[i + 1][1]))
    tunnels.append((y_planets[i][1], y_planets[i + 1][1]))
    tunnels.append((z_planets[i][1], z_planets[i + 1][1]))

# 터널 조합별로 비용 계산하기
data = []
for t in tunnels:
    data.append((t_cost(planets[t[0]], planets[t[1]]), (t[0], t[1])))

# 비용으로 정렬
data.sort()

count = 0
# 최소 비용 신장트리 만들기
result = 0
for d in data:
    a = d[1][0]
    b = d[1][1]
    cost = d[0]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        count += 1
        if count == n - 1:
            break

print(result)