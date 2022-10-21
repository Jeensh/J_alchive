# sys.setrecursionlimit(int(10e6))

# n개의 새로선, m개의 가로선
# 인접한 새로선 사이에는 가로선을 놓을 수 있음
# 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H

# 두 가로선이 연속하거나 접하면 안된다

# 사다리 게임흘 해서 i번 새로선의 결과가 i번이 나와야 한다
# 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값은?

# 모든 경우의 수 :
# 가로선을 1개씩 늘려가며 모든 위치에 놓는다
# 시뮬레이션을 돌려 각 번호가 각 번호로 도착하는지 확인한다
# 모두 각 번호로 도착하는 경우 탐색을 멈추고 추가한 가로선의 개수를 출력한다

MIN = int(1e9)

# count = 0

# 사다리게임 진행하여 확인하기
def game(n, h, graph):
    i = 1
    j = 1
    while i <= n:
        now = i
        while j <= h:
            # 왼쪽에 가로줄이 있을 때
            if now > 1 and graph[j][now - 1] == 1:
                now = now - 1
                j += 1
                continue
            # 오른쪽에 가로줄이 있을 때
            if now < n and graph[j][now] == 1:
                now = now + 1
                j += 1
                continue
            # 가로줄이 없을 때
            j += 1
        # 만약 도착 결과가 출발지점과 다르다면 유망하지 않음
        if now != i:
            return False
        j = 1
        i += 1
    return True

# 사다리 놓아보기
def solve(n, h, graph, level, target, x):
    global MIN, count
    # count += 1
    # print(count)
    if level == target:
        if game(n, h, graph):
            MIN = min(MIN, target)
        return
    for a in range(x, h + 1):
        for b in range(1, n):
            if graph[a][b] == 1:
                continue
            if b == 1:
                if graph[a][b + 1] == 1:
                    continue
            else:
                if graph[a][b + 1] == 1 or graph[a][b - 1] == 1:
                    continue
            graph[a][b] = 1
            solve(n, h, graph, level + 1, target, a)
            graph[a][b] = 0

# n, m, h 입력받기
n, m, h = map(int, input().split())

# 가로선의 정보 입력받기
# a, b : b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
# 가장 위에 있는 점선의 번호 : 1, 아래로 내려갈때마다 1씩 증가
graph = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(4):
    solve(n, h, graph, 0, i, 1)
if MIN == int(1e9):
    MIN = -1
print(MIN)