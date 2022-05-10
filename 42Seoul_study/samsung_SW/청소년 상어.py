def print_b(board):
    for i in board:
        print(i)

# 상 좌상 좌 좌하 하 하우 우 우상
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# (물고기 번호, (방향 벡터))
# 공간 정보 입력 받기
board = [[0] * 4 for i in range(4)]
for r in range(4):
    tmp = list(map(int, input().split()))
    for c in range(4):
        i = c * 2
        board[r][c] = (tmp[i], direction[tmp[i + 1] - 1])

# 결과
result = 0

# 상어 투입
result += board[0][0][0]
board[0][0] = ('s', board[0][0][1])

# 물고기 이동(순번대로)
def move_fish(board):
    global direction
    fish = 1
    while(fish < 17):
        flag = False
        for r in range(4):
            if flag or fish > 16:
                break
            for c in range(4):
                if flag or fish > 16:
                    break
                # 현재 순번의 물고기를 찾았을 떄
                if board[r][c] != 0 and board[r][c][0] == fish:
                    index = direction.index(board[r][c][1])
                    for i in range(1, 8):
                        # 현재 순번의 물고기가 이동할 경로가 공간 밖이면 반시계방향 45도 회전
                        if (r + board[r][c][1][0] < 0 or r + board[r][c][1][0] > 3) or (c + board[r][c][1][1] < 0 or c + board[r][c][1][1] > 3 or \
                            (board[r + board[r][c][1][0]][c + board[r][c][1][1]] != 0 and board[r + board[r][c][1][0]][c + board[r][c][1][1]][0] == 's')):
                            board[r][c] = (board[r][c][0], direction[(index + i) % 8])
                            continue
                        # 현재 순번의 물고기가 이동할 경로가 비어있거나 다른 물고기가 있으면 서로 자리이동 후 다음 물고기 탐색
                        if board[r + board[r][c][1][0]][c + board[r][c][1][1]] == 0 or board[r + board[r][c][1][0]][c + board[r][c][1][1]][0] != 's':
                            tmp = board[r][c]
                            board[r][c] = board[r + board[r][c][1][0]][c + board[r][c][1][1]]
                            board[r + tmp[1][0]][c + tmp[1][1]] = tmp
                            fish += 1
                            flag = True
                            break
                        flag = True
        if not flag:
            fish += 1

# 물고기 전부 이동
move_fish(board)

# 상어 찾기 함수
def find_shark(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] != 0 and board[r][c][0] == 's':
                return r, c

def solve(board, result_l):
    global result
    # 상어가 움직일 수 있는 경우의수 찾아가기
    can_shark_move = False
    s_r, s_c, = find_shark(board)
    for i in range(1, 4):
        # 상어가 이동할 경로가 공간을 벗어나는지 확인
        if (s_r + (board[s_r][s_c][1][0] * i) < 0 or s_r + (board[s_r][s_c][1][0] * i) > 3) or (s_c + (board[s_r][s_c][1][1] * i) < 0 or s_c + (board[s_r][s_c][1][1] * i) > 3):
            continue
        # 상어가 이동할 경로가 비어있는지 확인
        if board[s_r + (board[s_r][s_c][1][0] * i)][s_c + (board[s_r][s_c][1][1] * i)] == 0:
            continue
        board_l = []
        for l in board:
            board_l.append(l[:])
        # 상어가 이동할 경로에 물고기가 있다면
        tmp = board_l[s_r + (board_l[s_r][s_c][1][0] * i)][s_c + (board_l[s_r][s_c][1][1] * i)][0]
        board_l[s_r + (board_l[s_r][s_c][1][0] * i)][s_c + (board_l[s_r][s_c][1][1] * i)] = ('s', board_l[s_r + (board_l[s_r][s_c][1][0] * i)][s_c + (board_l[s_r][s_c][1][1] * i)][1])
        board_l[s_r][s_c] = 0
        move_fish(board_l)
        solve(board_l, result_l + tmp)
        can_shark_move = True
    # 상어가 움직일 수 없다면
    if (not can_shark_move):
        result = max(result_l, result)

solve(board, result)
print(result)