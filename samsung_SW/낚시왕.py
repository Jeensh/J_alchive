# r x c 격자판
# 낚시왕의 첫 위치는 1번열의 한칸 왼쪽 (-1)

# 다음은 1초 동안 일어나는 일, 아래 적힌 순서대로 일어난다
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸으로 이동하면 이동을 멈춘다 (c)
#   1. 낚시왕이 오른쪽으로 한 칸 이동한다
#   2. 낚시왕이 있는 열에 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다
#   3. 상어가 이동한다

# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초 이다
# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다

# 상어가 이동을 마친 후에 한 칸에 상어가 두마리 이상 있다면, 가장 큰 상어가 나머지 상어를 모두 잡아먹는다
# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 상어 잡기
def fishing(board, pos, r):
    for x in range(r):
        if board[x][pos]:
            z, s, d = board[x][pos]
            board[x][pos] = False
            return z
    return 0

# 상어 이동하기
def move(board, r, c):
    상어 = []
    for x in range(r):
        for y in range(c):
                # 각 상어
                if board[x][y]:
                    z, s, d = board[x][y]
                    nx = x
                    ny = y
                    t_s = s
                    while s > 0:
                        # 방향이 위쪽 이라면
                        if d == 1:
                            # 벽까지의 거리
                            to_wall = nx
                            # 이동해야할 거리가 벽까지의 거리보다 많다면
                            if to_wall < s:
                                # 벽까지 이동하고 방향 전환 후 coutinue
                                nx = 0
                                d = 2
                                s -= to_wall
                                continue
                            # 이동해야할 거리가 벽까지의 거리보다 적다면
                            else:
                                nx -= s
                                break
                        # 방향이 아래쪽 이라면
                        elif d == 2:
                            # 벽까지의 거리
                            to_wall = (r - 1) - nx
                            # 이동해야할 거리가 벽까지의 거리보다 많다면
                            if to_wall < s:
                                # 벽까지 이동하고 방향 전환 후 coutinue
                                nx = r - 1
                                d = 1
                                s -= to_wall
                                continue
                            # 이동해야할 거리가 벽까지의 거리보다 적다면
                            else:
                                nx += s
                                break
                        # 방향이 오른쪽 이라면
                        elif d == 3:
                            # 벽까지의 거리
                            to_wall = (c - 1) - ny
                            # 이동해야할 거리가 벽까지의 거리보다 많다면
                            if to_wall < s:
                                # 벽까지 이동하고 방향 전환 후 coutinue
                                ny = c - 1
                                d = 4
                                s -= to_wall
                                continue
                            # 이동해야할 거리가 벽까지의 거리보다 적다면
                            else:
                                ny += s
                                break
                        # 방향이 왼쪽 이라면
                        elif d == 4:
                            # 벽까지의 거리
                            to_wall = ny
                            # 이동해야할 거리가 벽까지의 거리보다 많다면
                            if to_wall < s:
                                # 벽까지 이동하고 방향 전환 후 coutinue
                                ny = 0
                                d = 3
                                s -= to_wall
                                continue
                            # 이동해야할 거리가 벽까지의 거리보다 적다면
                            else:
                                ny -= s
                                break
                    상어.append((z, t_s, d, nx, ny))

    # 상어 이동하기
    after_board = [[False] * c for i in range(r)]
    상어.sort()
    상어.reverse()
    # print(상어)
    for shark in 상어:
        z, s, d, x, y = shark
        if after_board[x][y]:
            continue
        after_board[x][y] = ((z, s, d))
    return after_board

# r, c, 상어의 수 m 입력받기
r, c, m = map(int, input().split())

# 맵 만들기
board = [[False] * c for i in range(r)]

# 상어의 정보 입력받기
# (x, y) 위치, s : 속력, d : 이동방향, z : 크기
# d: 1,2,3,4 - 위 아래 오른쪽 왼쪽
for i in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = ((z, s, d))

# 진행
total = 0
for pos in range(c):
    # print('-----')
    # for i in board:
    #     print(i)

    total += fishing(board, pos, r)
    board = move(board, r, c)
print(total)
