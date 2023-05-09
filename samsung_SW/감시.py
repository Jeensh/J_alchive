# n x m 직사각형
# 사무실에는 총 k개의 CCTV
# 1. 한 쪽 방향
# 1. 양 쪽 방향
# 1. 직각 방향
# 1. 3방향
# 1. 4방향

# CCTV는 감시하는 방향에 있는 칸 전체 감시 가능
# 벽을 넘어서는 감시 불가능
# CCTV는 90도 방향으로 회전 가능

# 지도에서 0은 빈칸, 6은 벽, 1~5는 CCTV의 번호
# 사무실의 크기와 상태, CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서 사각지대의 최소 크기를 구하는 프로그램 작성

# 방향
from copy import deepcopy


상 = (-1, 0)
하 = (1, 0)
좌 = (0, -1)
우 = (0, 1)

# 각 CCTV 별 방향
CCTV = [[]]
CCTV.append([ [상], [하], [좌], [우] ])
CCTV.append([ [상, 하], [좌, 우] ])
CCTV.append([ [상, 우], [우, 하], [하, 좌], [좌, 상] ])
CCTV.append([ [좌, 상, 우], [상, 우, 하], [우, 하, 좌], [하, 좌, 상] ])
CCTV.append([ [상, 하, 좌, 우] ])

# 최소 사각지대
result = 10000000

# 맵 출력
def p_board(board):
    print('------------------------')
    for line in board:
        print(line)

# 사무실안의 사각지대 크기 반환 함숨
def total_blind_spot(board):
    total = 0
    for line in board:
        total += line.count(0)
    return total


def solve(board, n, m, CCTV_spot, CCTV_len, level):
    global CCTV, result
    if level == CCTV_len:
        result = min(result, total_blind_spot(board))
        # p_board(board)
        # print(result)
        return
    x, y =  CCTV_spot[level]
    now = board[x][y]
    board_l = deepcopy(board)
    for case in CCTV[now]:
        for d in case:
            nx = x + d[0]
            ny = y + d[1]
            while nx >= 0 and nx < n and ny >= 0 and ny < m:
                n_tmp = board_l[nx][ny]
                if n_tmp == 6:
                    break
                elif n_tmp == 0:
                    board_l[nx][ny] = '#'
                nx += d[0]
                ny += d[1]
        solve(board_l, n, m, CCTV_spot, CCTV_len, level + 1)
        board_l = deepcopy(board)

# n, m 입력받기
n, m = map(int, input().split())

# 사무실 입력받기
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# CCTV 위치 및 개수 구하기
CCTV_spot = []
for x in range(n):
    for y in range(m):
        now =  board[x][y]
        if now >= 1 and now <= 5:
            CCTV_spot.append(((x, y)))
CCTV_len = len(CCTV_spot)

# 최소 사각지대 구하기
solve(board, n, m, CCTV_spot, CCTV_len, 0)

print(result)