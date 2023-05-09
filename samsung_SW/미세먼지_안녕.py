# R x C인 격자판
# (r, c)에 는 각 칸의 미세먼지 양이 있음

# 공기청정기는 항상 1번열에 설치되어 있음
#   - 크기는 두 칸을 차지
#   - 청청기가 있는 칸에는 미세먼지가 없음

# 1초 동안 아래의 일이 순서대로 일어남
# 1. 미세먼지가 확산, 미세먼지가 있는 모든 칸에서 동시에 일어남
#   - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
#   - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 x
#   - 확산되는 양은 A(r, c)/5이고 소수점은 버림
#   - A(r, c)에 남은 미세먼지의 양은 A(r, c) - (A(r, c)/5 * (확산된 방향의 개수))
# 2. 공기청청기가 작동
#   - 공기청청기에서 바람이 나옴
#   - 위쪽 공기청청기의 바람은 반시계방향으로 순환하고, 아래쪽 공기 청청기의 바람은 시계방향으로 순환
#   - 바람이 불면 미세 먼지가 바람의 방향대로 모두 한칸씩 이동
#   - 공기청청기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청청기로 들어간 미세먼지는 모두 정화됨

# 방향
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

# 위쪽 순환
def up_cycle(board, x, y, r, c):
    nx = x
    ny = y + 1
    past = 0
    tmp = 0
    # 오른쪽 끝까지 진행
    while ny < c - 1:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        ny += 1
    # 위쪽 끝까지 진행
    while nx > 0:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        nx -= 1
    # 왼쪽 끝까지 진행
    while ny > 0:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        ny -= 1
    # 에어컨 위까지 진행
    while nx < x:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        nx += 1

# 아래쪽 순환
def down_cycle(board, x, y, r, c):
    nx = x
    ny = y + 1
    past = 0
    tmp = 0
    # 오른쪽 끝까지 진행
    while ny < c - 1:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        ny += 1
    # 아래쪽 끝까지 진행
    while nx < r - 1:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        nx += 1
    # 왼쪽 끝까지 진행
    while ny > 0:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        ny -= 1
    # 에어컨 아래까지 진행
    while nx > x:
        tmp = board[nx][ny]
        board[nx][ny] = past
        past = tmp
        nx -= 1

# 미세먼지 확산 시키기
def spread(board, r, c):
    # 이동한 미세먼지들을 임시로 담을 행렬
    tmp = [[0] * c for i in range(r)]

    for x in range(r):
        for y in range(c):
            # 에어컨 있는 곳이라면 스킵
            미세먼지 = board[x][y]
            if 미세먼지 == -1 or 미세먼지 == 0:
                continue
            else:
                to_spread = 미세먼지 // 5
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        count += 1
                        tmp[nx][ny] += to_spread
                board[x][y] -= to_spread * count
    for x in range(r):
        for y in range(c):
            if board[x][y] == -1:
                continue
            board[x][y] += tmp[x][y]

# r, c, t 입력받기
r, c, t = map(int, input().split())

# 맵 입력받기, 공기청정기 : -1, 나머지는 미세먼지 값
board = []
for i in range(r):
    board.append(list(map(int, input().split())))

# 공기청정기 위치 가져오기
공기청정기 = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            공기청정기.append((i, j))

up_x = 공기청정기[0][0]
up_y = 공기청정기[0][1]
down_x = 공기청정기[1][0]
down_y = 공기청정기[1][1]

# 진행
for i in range(t):
    spread(board, r, c)
    up_cycle(board, up_x, up_y, r, c)
    down_cycle(board, down_x, down_y, r, c)

# 결과 출력
result = 0
for x in range(r):
    for y in range(c):
        if board[x][y] == -1:
            continue
        result += board[x][y]
print(result)
