# 자연수 N 입력받기
from copy import deepcopy


n = int(input())

# 지도 입력받기
board = []
blank = [] # 빈칸의 위치를 담을 리스트
teacher = [] # 선생님의 위치를 담을 리스트
student = [] # 학생의 위치를 담을 리스트
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'X':
            blank.append((i, j))
        elif board[i][j] == 'S':
            student.append((i, j))
        elif board[i][j] == 'T':
            teacher.append((i, j))

# 조합 함수
def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - (n - 1)):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

# 벽을 놓는 경우의 수 구하기
blank_comb = comb(blank, 3)

# 들키는 학생이 있는지 확인하는 함수
def catched(board, teacher):
    for t_pos in teacher:
        # 위쪽 확인
        for i in range(1, n):
            if t_pos[0] - i < 0 or board[t_pos[0] - i][t_pos[1]] == 'O':
                break
            if board[t_pos[0] - i][t_pos[1]] == 'S':
                return True
        # 아래 확인
        for i in range(1, n):
            if t_pos[0] + i >= n or board[t_pos[0] + i][t_pos[1]] == 'O':
                break
            if board[t_pos[0] + i][t_pos[1]] == 'S':
                return True
        # 좌측 확인
        for i in range(1, n):
            if t_pos[1] - i < 0 or board[t_pos[0]][t_pos[1] - i] == 'O':
                break
            if board[t_pos[0]][t_pos[1] - i] == 'S':
                return True
        # 우측 확인
        for i in range(1, n):
            if t_pos[1] + i >= n or board[t_pos[0]][t_pos[1] + i] == 'O':
                break
            if board[t_pos[0]][t_pos[1] + i] == 'S':
                return True
    return False

# 벽을 놓는 경우의 수 마다 확인
flag = True
for walls in blank_comb:
    board_tmp = deepcopy(board)
    for w in walls:
        board_tmp[w[0]][w[1]] = 'O'
    if not catched(board_tmp, teacher):
        print("YES")
        flag = False
        break
if flag:
    print("NO")