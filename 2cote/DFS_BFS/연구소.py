# 0은 빈칸
# 1은 벽
# 2는 바이러스
from copy import deepcopy
from itertools import combinations

# 상하좌우
fx = [-1, 1, 0, 0]
fy = [0, 0, -1, 1]

# 지도 출력
def print_board(m):
    print("*-------------------------------------------------*")
    for i in m:
        print(i)

# 조합 함수
def comb(arr, r):
    result = []
    if r > len(arr):
        return result

    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - (r - 1)):
            for j in comb(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)
    return result

# 바이러스 채우기
def spread(v, board, n, m):
    if board[v[0]][v[1]] == 0:
        board[v[0]][v[1]] = 2
        for i in range(4):
            x = v[0] + fx[i]
            y = v[1] + fy[i]
            if x >= 0 and x < n and y >=0 and y < m and board[x][y] == 0:
                spread((x, y), board, n, m)


# 세로길이 N, 가로길이 M 입력받기
n, m = map(int, input().split())

# 연구소 지도 입력받기
board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

# 바이러스 위치
virus = []

# 연구소의 벽을 놓을 수 있는 각 위치
position = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        if board[i][j] == 0:
            position.append((i, j))

# 벽의 위치 경우를 담은 리스트
comb_list = comb(position, 3)
# comb_list = list(combinations(position, 3))

# 가장 큰 안전 영역
MAX = 0

# 각 경우 마다 안전 영역 구하기
for pos in comb_list:
    tmp_board = deepcopy(board)
    # 벽 세우기
    for p in pos:
        tmp_board[p[0]][p[1]] = 1
    # 바이러스 채우기
    for v in virus:
        tmp_board[v[0]][v[1]] = 0
        spread(v, tmp_board, n, m)
    # 안전영역 구하기
    count = 0
    for i in tmp_board:
        for j in i:
            if j == 0:
                count += 1
    # if MAX < count:
    #     print_board(tmp_board)
    #     print(count)
    #     print(pos)
    #     MAX = count
    MAX = max(MAX, count)

print(MAX)
