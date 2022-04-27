
# 종이의 세로크기 N, 종이의 가로 크기 M 입력받기
N, M = map(int, input().split())

# 맵 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 우 하 좌
fx = [0, 1, 0]
fy = [1, 0, -1]

# 최대값
MAX = 0

# 테트로미노 계산(뻐큐모양 제외)
def solve(board, count, sum, pos, visited):
    print(visited)
    global fx, fy, MAX
    visited_l = visited[:]
    visited_l.append(pos)
    sum_l = sum + board[pos[0]][pos[1]]
    if count == 4:
        visited = []
        MAX = max(MAX, sum_l)
        return
    # 하 좌 우
    for i in range(3):
        if (pos[0] + fx[i] < 0 or pos[0] + fx[i] > N - 1) or (pos[1] + fy[i] < 0 or pos[1] + fy[i] > M - 1) or (pos[0] + fx[i], pos[1] + fy[i]) in visited:
            continue
        solve(board, count + 1, sum_l, (pos[0] + fx[i], pos[1] + fy[i]), visited_l)

# 뻐큐모양 테트로미노 계산
def f_solve(board, pos):
    global MAX
    #좌
    if not (pos[0] + 2 > N - 1 or pos[1] - 1 < 0):
        s = board[pos[0]][pos[1]] + board[pos[0] + 1][pos[1]] + board[pos[0] + 2][pos[1]] + board[pos[0] + 1][pos[1] - 1]
        MAX = max(MAX, s)
    #상
    if not (pos[0] - 1 < 0 or pos[1] + 2 > M - 1):
        s = board[pos[0]][pos[1]] + board[pos[0]][pos[1] + 1] + board[pos[0]][pos[1] + 2] + board[pos[0] - 1][pos[1] + 1]
        MAX = max(MAX, s)
    #우
    if not (pos[0] + 2 > N - 1 or pos[1] + 1 > M - 1):
        s = board[pos[0]][pos[1]] + board[pos[0] + 1][pos[1]] + board[pos[0] + 2][pos[1]] + board[pos[0] + 1][pos[1] + 1]
        MAX = max(MAX, s)
    #하
    if not (pos[0] + 1 > N - 1 or pos[1] + 2 > M - 1):
        s = board[pos[0]][pos[1]] + board[pos[0]][pos[1] + 1] + board[pos[0]][pos[1] + 2] + board[pos[0] + 1][pos[1] + 1]
        MAX = max(MAX, s)

for i in range(N):
    for j in range(M):
        solve(board, 1, 0, (i, j), [])
        f_solve(board, (i, j))

print(MAX)