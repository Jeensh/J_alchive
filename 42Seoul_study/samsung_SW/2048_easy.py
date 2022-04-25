import sys
input = sys.stdin.readline

# 보드 출력
def print_b(board):
    for b in board:
        print(b)

# 보드의 크기 N입력 받기
N = int(input())

# 보드 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

MAX = 0

# 위쪽으로 슬라이드
def slide_up(board):
    global N
    # row
    for i in range(N):
        # col
        for j in range(N):
            # 아래에 있는 원소들 탐색
            for k in range(1, N - i):
                # 만약 아래에 있는 숫자가 같은 숫자가 아닌데 0도 아닌경우
                if board[i][j] != board[i + k][j] and board[i + k][j] != 0:
                    break
                # 아래에 같은 숫자가 있다면
                if board[i][j] == board[i + k][j]:
                    board[i][j] *= 2
                    board[i + k][j] = 0
                    break
    # 상단으로 전부 끌어 올리기
    for i in range(1, N):
        for j in range(N):
            for k in range(i, 0, -1):
                if board[i][j] == 0:
                    break
                if board[i - k][j] == 0:
                    board[i][j], board[i - k][j] = board[i - k][j], board[i][j]
                    break

# 아래쪽으로 슬라이드
def slide_down(board):
    global N
    # row
    for i in range(N - 1, -1, -1):
        # col
        for j in range(N - 1, -1, -1):
            # 위에 있는 원소들 탐색
            for k in range(1, i + 1):
                # 만약 위에 있는 숫자가 같은 숫자가 아닌데 0도 아닌경우
                if board[i][j] != board[i - k][j] and board[i - k][j] != 0:
                    break
                # 위에 같은 숫자가 있다면
                if board[i][j] == board[i - k][j]:
                    board[i][j] *= 2
                    board[i - k][j] = 0
                    break
    # 하단으로 전부 끌어 내리기
    for i in range(N - 2, -1, -1):
        for j in range(N - 1, -1, -1):
            for k in range(N - 1 - i):
                if board[i][j] == 0:
                    break
                if board[N - 1 - k][j] == 0:
                    board[i][j], board[N - 1 - k][j] = board[N - 1 - k][j], board[i][j]
                    break

# 왼쪽으로 슬라이드
def slide_left(board):
    global N
    # row
    for i in range(N):
        # col
        for j in range(N):
            # 오른쪽에 있는 원소들 탐색
            for k in range(1, N - j):
                # 만약 오른쪽에 있는 숫자가 같은 숫자가 아닌데 0도 아닌경우
                if board[i][j] != board[i][j + k] and board[i][j + k] != 0:
                    break
                # 오른쪽에 같은 숫자가 있다면
                if board[i][j] == board[i][j + k]:
                    board[i][j] *= 2
                    board[i][j + k] = 0
                    break
    # 좌측으로 전부 쓸기
    for i in range(N):
        for j in range(1, N):
            for k in range(j, 0, -1):
                if board[i][j] == 0:
                    break
                if board[i][j - k] == 0:
                    board[i][j], board[i][j - k] = board[i][j - k], board[i][j]
                    break

# 오른쪽으로 슬라이드
def slide_right(board):
    global N
    # row
    for i in range(N - 1, -1, -1):
        # col
        for j in range(N - 1, -1, -1):
            # 왼쪽에 있는 원소들 탐색
            for k in range(1, j + 1):
                # 만약 왼쪽에 있는 숫자가 같은 숫자가 아닌데 0도 아닌경우
                if board[i][j] != board[i][j - k] and board[i][j - k] != 0:
                    break
                # 왼쪽에 같은 숫자가 있다면
                if board[i][j] == board[i][j - k]:
                    board[i][j] *= 2
                    board[i][j - k] = 0
                    break
    # 우측으로 전부 쓸기
    for i in range(N - 1, -1, -1):
        for j in range(N - 2, -1, -1):
            for k in range(N - 1 - j):
                if board[i][j] == 0:
                    break
                if board[i][N - 1 - k] == 0:
                    board[i][j], board[i][N - 1 - k] = board[i][N - 1 - k], board[i][j]
                    break

# 가장 큰 블록 찾기
def find_biggest_block(board):
    global N
    biggest = 0
    for i in range(N):
        for j in range(N):
            biggest = max(biggest, board[i][j])
    return biggest

biggest_block = 0

def solve(board, count):
    global biggest_block
    if count == 6:
        biggest_block = max(biggest_block, find_biggest_block(board))
        return
    # 상
    board_l = []
    for l in board:
        board_l.append(l[:])
    slide_up(board_l)
    solve(board_l, count + 1)
    # 하
    board_l = []
    for l in board:
        board_l.append(l[:])
    slide_down(board_l)
    solve(board_l, count + 1)
    # 좌
    board_l = []
    for l in board:
        board_l.append(l[:])
    slide_left(board_l)
    solve(board_l, count + 1)
    # 우
    board_l = []
    for l in board:
        board_l.append(l[:])
    slide_right(board_l)
    solve(board_l, count + 1)

solve(board, 1)
print(biggest_block)
