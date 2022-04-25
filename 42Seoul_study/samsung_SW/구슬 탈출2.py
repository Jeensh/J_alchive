
def print_board(board):
    for i in board:
        print(i)

# 반환값 1 : 아무 공도 구멍에 들어가지 않음
# 반환값 2 : 빨간공이 먼저 구멍에 들어감
# 반환값 3 : 파란공이 먼저 or 같이 구멍에 들어감
# 왼쪽 기울이기
def tilt_left(board, row, col):
    something_moved = True
    flag1 = False
    flag2 = False
    while (something_moved):
        something_moved = False
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'B':	# 파란공
                    if board[i][j - 1] == 'O':
                        flag1 = True
                        board[i][j] = '.'
                    elif board[i][j - 1] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i][j - 1] = 'B'
                if board[i][j] == 'R':	# 빨간공
                    if board[i][j - 1] == 'O':
                        flag2 = True
                        board[i][j] = '.'
                    elif board[i][j - 1] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i][j - 1] = 'R'
    if flag1:
        return 3
    elif flag2:
        return 2
    else:
        return 1

# 오른쪽 기울이기
def tilt_right(board, row, col):
    something_moved = True
    flag1 = False
    flag2 = False
    while (something_moved):
        something_moved = False
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'B':	# 파란공
                    if board[i][j + 1] == 'O':
                        flag1 = True
                        board[i][j] = '.'
                    elif board[i][j + 1] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i][j + 1] = 'B'
                if board[i][j] == 'R':	# 빨간공
                    if board[i][j + 1] == 'O':
                        flag2 = True
                        board[i][j] = '.'
                    elif board[i][j + 1] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i][j + 1] = 'R'
    if flag1:
        return 3
    elif flag2:
        return 2
    else:
        return 1

# 위로 기울이기
def tilt_up(board, row, col):
    something_moved = True
    flag1 = False
    flag2 = False
    while (something_moved):
        something_moved = False
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'B':	# 파란공
                    if board[i - 1][j] == 'O':
                        flag1 = True
                        board[i][j] = '.'
                    elif board[i - 1][j] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i - 1][j] = 'B'
                if board[i][j] == 'R':	# 빨간공
                    if board[i - 1][j] == 'O':
                        flag2 = True
                        board[i][j] = '.'
                    elif board[i - 1][j] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i - 1][j] = 'R'
    if flag1:
        return 3
    elif flag2:
        return 2
    else:
        return 1

# 아래로 기울이기
def tilt_down(board, row, col):
    something_moved = True
    flag1 = False
    flag2 = False
    while (something_moved):
        something_moved = False
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == 'B':	# 파란공
                    if board[i + 1][j] == 'O':
                        flag1 = True
                        board[i][j] = '.'
                    elif board[i + 1][j] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i + 1][j] = 'B'
                if board[i][j] == 'R':	# 빨간공
                    if board[i + 1][j] == 'O':
                        flag2 = True
                        board[i][j] = '.'
                    elif board[i + 1][j] == '.':
                        something_moved = True
                        board[i][j] = '.'
                        board[i + 1][j] = 'R'
    if flag1:
        return 3
    elif flag2:
        return 2
    else:
        return 1

result = 11

def dfs(board, count):
    global result
    if count > 10:
        return
    board_l = []
    for l in board:
        board_l.append(l[:])
    tmp = tilt_up(board_l, N, M)
    if tmp == 2:
        result = min(result, count)
        return
    elif tmp == 1:
        dfs(board_l, count + 1)

    board_l = []
    for l in board:
        board_l.append(l[:])
    tmp = tilt_down(board_l, N, M)
    if tmp == 2:
        result = min(result, count)
        return
    elif tmp == 1:
        dfs(board_l, count + 1)

    board_l = []
    for l in board:
        board_l.append(l[:])
    tmp = tilt_left(board_l, N, M)
    if tmp == 2:
        result = min(result, count)
        return
    elif tmp == 1:
        dfs(board_l, count + 1)

    board_l = []
    for l in board:
        board_l.append(l[:])
    tmp = tilt_right(board_l, N, M)
    if tmp == 2:
        result = min(result, count)
        return
    elif tmp == 1:
        dfs(board_l, count + 1)

# 보드의 세로(N), 가로(M) 크기 입력받기
N, M = map(int, input().split())

# 보드 초기화
board = []

# 보드 입력받기
for i in range(N):
    board.append([])
    tmp = input()
    for j in range(M):
        board[i].append(tmp[j])

dfs(board, 1)

if result > 10:
    print(-1)
else:
    print(result)