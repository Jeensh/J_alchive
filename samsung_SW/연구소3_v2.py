# 방향
from collections import deque
from copy import deepcopy


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# comb
def comb(arr, n):
    result = []
    if len(arr) < n:
        return result
    if n == 1:
        for item in arr:
            result.append([item])
    elif n > 1:
        for i in range(len(arr) - (n - 1)):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

# 바이러스가 퍼졌는지 체크
def check_maps(maps):
    for x in range(n):
        for y in range(n):
            if maps[x][y] == 0:
                return -1
    return 0

# 바이러스 퍼트리기
def bfs(start, maps, n):
    visited = [[0] * n for i in range(n)]
    maps = deepcopy(maps)
    dq = deque()
    dq.extend(start)

    cnt = 0
    while dq:
        x, y, d = dq.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] != 1:
                    visited[nx][ny] = 1
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = 2
                        cnt = d + 1
                    dq.append((nx, ny, d + 1))
    val = check_maps(maps)
    # print('--------------')
    # for i in maps:
    #     print(i)
    if val == 0:
        return cnt
    else:
        return -1


# n, m 입력받기
n, m = map(int, input().split())
maps = []
virus = []

# 맵 입력받기
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 2:
            virus.append((i, j, 0))
    maps.append(a)

time = 10000
cases = comb(virus, m)

for case in cases:
    res = bfs(case, maps, n)
    if time > res and res != -1:
        time = res

if time == 10000:
    print(-1)
else:
    print(time)