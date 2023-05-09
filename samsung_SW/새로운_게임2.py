# n x n 체스판
# 사용하는 말의 개수 k
# 말은 원판 모양, 하나의 말 위에 다른 말을 올릴 수 있음
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠됨

# 게임은 체스판 위에 말 k개를 놓고 시작
# 말은 1~k번 까지 번호가 매겨져 있고, 이동 방향도 정해져 있다 (위 아래 왼 오른)

# 턴 한번은 1번 말부터 k번 말까지 순서대로 이동시키는 것
# 한 말이 이동할 때, 위에 올려져 있는 말도 함께 이동
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다

# A번 말이 이동하려는 칸이
#   - 흰색인 경우에는 그 칸으로 이동, 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓음
#       - A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동
#       - 예를 들어, A B C로 쌓여있고, 이동하려는 칸에 D E가 있는 경우 이동후 D E A B C 가 된다
#   - 빨간색인 경우 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꿈
#       - A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C B A가 된다
#       - A D F G가 이동하고, 이동하려는 칸에  E C B로 있는 경우에는 E C B G F D A가 된다
#   - 파란색인 경우에는 A번 말의 이동방향을 반대로 하고 한 칸 이동한다, 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다
#   - 체스판을 벗어나는 경우에은 파란색과 같은 경우이다

# 게임이 종료되는 턴의 번호를 출력하자
# 그 값이 1000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다

# 방향 : 우 좌 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 반대 방향 좌 우 하 상
reverse_d = [1, 0, 3, 2]

# 색
흰 = 0
빨 = 1
파 = 2

# 말 이동시키기
def move(i, board_color, board_unit, unit, n):
    global 흰, 빨, 파
    # 이동시킬 말의 정보
    x, y, d = unit[i]
    # 이동할 위치 확인
    nx = x + dx[d]
    ny = y + dy[d]
    # 이동할 위치가 흰색
    if 0 <= nx < n and 0 <= ny < n:
        if board_color[nx][ny] == 흰:
            # 이동할 말이 혼자인 경우
            if len(board_unit[x][y]) == 1:
                board_unit[x][y].pop()
                board_unit[nx][ny].append(i)
                unit[i] = (nx, ny, d)
            # 이동할 말이 혼자가 아닌 경우
            else:
                # 해당 위치에서 말의 인덱스
                idx = board_unit[x][y].index(i)
                len_t = len(board_unit[x][y])
                for t in range(idx, len_t):
                    u_i = board_unit[x][y][t]
                    x_t, y_t, d_t = unit[u_i]
                    board_unit[nx][ny].append(board_unit[x][y][t])
                    unit[u_i] = (nx, ny, d_t)
                for _ in range(len_t - idx):
                    board_unit[x][y].pop()
            # 이동한 위치의 말이 4개 이상인 경우 종료
            if len(board_unit[nx][ny]) >= 4:
                return False
    # 이동할 위치가 빨간색
        if board_color[nx][ny] == 빨:
            # 이동할 말이 혼자인 경우
            if len(board_unit[x][y]) == 1:
                board_unit[x][y].pop()
                board_unit[nx][ny].append(i)
                unit[i] = (nx, ny, d)
            # 이동할 말이 혼자가 아닌 경우
            else:
                # 해당 위치에서 말의 인덱스
                idx = board_unit[x][y].index(i)
                len_t = len(board_unit[x][y])
                for t in range(len_t - 1, idx - 1, -1):
                    u_i = board_unit[x][y][t]
                    x_t, y_t, d_t = unit[u_i]
                    board_unit[nx][ny].append(board_unit[x][y][t])
                    unit[u_i] = (nx, ny, d_t)
                for _ in range(len_t - idx):
                    board_unit[x][y].pop()
            if len(board_unit[nx][ny]) >= 4:
                return False
    # 이동할 위치가 파랑
        if board_color[nx][ny] == 파:
            # 방향 반대로 바꾸기
            d = reverse_d[d]
            nx = x + dx[d]
            ny = y + dy[d]
            unit[i] = (x, y, d)
            # 반대로 바꾸고 이동할 곳이 흰이나 빨인 경우에만 이동
            if 0 <= nx < n and 0 <= ny < n:
                if board_color[nx][ny] == 빨 or board_color[nx][ny] == 흰:
                    return move(i, board_color, board_unit, unit, n)
    # 이동할 위치가 밖
    else:
        # 방향 반대로 바꾸기
            d = reverse_d[d]
            nx = x + dx[d]
            ny = y + dy[d]
            unit[i] = (x, y, d)
            # 반대로 바꾸고 이동할 곳이 흰이나 빨인 경우에만 이동
            if 0 <= nx < n and 0 <= ny < n:
                if board_color[nx][ny] == 빨 or board_color[nx][ny] == 흰:
                    return move(i, board_color, board_unit, unit, n)
    return True

# n, k 입력받기
n, k = map(int, input().split())

# 체스판 입력받기
board_color = []
for i in range(n):
    board_color.append(list(map(int, input().split())))

# 말의 정보 입력받기
board_unit = [[[] for i in range(n)] for i in range(n)]
unit = [0] * (k + 1)
for i in range(k):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    unit[i + 1] = (x, y, d)
    board_unit[x][y].append(i + 1)

# 진행
i = 1
turn = 1
while 1:
    if i == k + 1:
        i = 1
        turn += 1
        if turn > 1000:
            turn = -1
            break
        continue
    if not move(i, board_color, board_unit, unit, n):
        break
    i += 1

print(turn)