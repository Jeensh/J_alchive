from collections import deque
# 토마토 : 익은 토마토, 익지 않은 토마토
# 하루가 지나면, 익은 토마토의 인접한 위치에 있는 익지 않은 토마토는 익는다

# 창고에 보관된 토마토가 며칠이 지나면 다 익는지 구해야 함

# 상자 크기 n x m
# h : 상자 개수

# 방향 : 상 하 좌 우 위 아래 (x, y, z)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

result = 0

# 토마토 익게 만들기
# 1 : 익은 토마토, 0, 익지 않은 토마토, -1 토마토가 없는 곳
def move(box, riped, n, m, h):
    global result
    q = deque(riped)
    while q:
        day, z, x, y = q.pop()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    result = max(result, day + 1)
                    q.appendleft((day + 1, nz, nx, ny))

# 토마토가 모두 익었는지 확인
def check(box, n, m, h):
    global result
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if box[z][x][y] == 0:
                    result = -1
                    return


# n, m, h 입력받기
m, n, h = map(int, input().split())

# 상자 정보 입력받기
# [z][x][y]
box = [[[] for i in range(n)] for i in range(h)]
riped = []
for z in range(h):
    for x in range(n):
        box[z][x] = list(map(int, input().split()))
        for y in range(m):
            if box[z][x][y] == 1:
                riped.append((0, z, x, y))

move(box, riped, n, m, h)
check(box, n, m, h)
print(result)