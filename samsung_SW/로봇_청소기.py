# N,M 크기의 직사각형 공간
# 청소기는 바라보는 방향이 있음
# 로봇 청소기가 청소하는 칸의 개수 구하기

# 방향 : 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# n, m 입력받기
n, m = map(int, input().split())

# 로봇 청소기가 있는 칸의 좌표와 방향 입력받기
x, y, d_tmp = map(int, input().split())
if d_tmp == 0:
    d_now = 0
elif d_tmp == 1:
    d_now = 3
elif d_tmp == 2:
    d_now = 2
elif d_tmp == 3:
    d_now = 1

# 공간 정보 입력받기 빈칸 : 0, 벽 : 1
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 청소기 작동
count = 0
backed = False
while 1:
    # print('----')
    # print(x, y, d_now)
    # for i in board:
    #     print(i)
    if not backed and board[x][y] == 0:
        count += 1
        board[x][y] = 2

    backed = False
    can_move = False
    for i in range(1, 5):
        nx = x + dx[(d_now + i) % 4]
        ny = y + dy[(d_now + i) % 4]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if board[nx][ny] == 0:
                x = nx
                y = ny
                d_now = (d_now + i) % 4
                can_move = True
                break

    if can_move:
        continue
    else:
        tx = x + dx[(d_now + 2) % 4]
        ty = y + dy[(d_now + 2) % 4]
        if board[tx][ty] != 1:
            x = tx
            y = ty
            backed = True
            continue
        else:
            break

print(count)
