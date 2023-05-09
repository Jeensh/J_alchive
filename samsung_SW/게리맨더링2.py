# 재현시 : n x n 크기
# 5개의 선거구로 나누어야 함
# 선거구는 구역을 적어도 하나 포함해야 함
# 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 함

# 선거구를 나누는 방법
#   1. 기준점 (x, y)와 경계의 길이 d1, d2를 정한다
#   2. 다음 칸은 경계선이다
#       1. (x, y),(x+1, y-1)...(x+d1, y-d1)
#       2. (x, y),(x+1, y+1)...(x+d2, y+d2)
#       3. (x+d1, y-d1),(x+d1+1, y-d1+1) ... (x+d1+d2, y-d1+d2)
#       4. (x+d2, y+d2),(x+d2+1, y+d2-1) ... (x+d2+d1, y+d2-d1)
#   3. 경계선과 경계선의 안에 포함되어 있는 곳은 5번 선거구이다
#   4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선서구 번호는 다음 기준을 따른다
#       1. 1번 선거구 : 1 <= r < x + d1, 1 <= c <= y
#       1. 2번 선거구 : 1 ≤ r ≤ x+d2, y < c ≤ N
#       1. 3번 선거구 : x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
#       1. 4번 선거구 : x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

# 구역 (x, y)의 인구는 A[x][y]이고, 선거구의 인구는 선거구에 포함된 인구를 모두 합한 값이다
# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구차이의 최솟값을 구해보자

# 선거구 나누기
def get_map(n, x, y, d1, d2):
    board = [[0] * (n + 2) for i in range(n + 2)]
    # 경계선과 5번 선거구 나누기
    for i in range(d1 + 1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        board[x + i][y + i] = 5
        board[x + d1 + i][y -d1 +i] = 5
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(y - d1, y + d2 + 1):
            if board[i][j] == 5 and not flag:
                flag = True
            elif board[i][j] == 5 and flag:
                flag = False
            if flag:
                board[i][j] = 5

    # 1번 선거구 설정
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if board[r][c] == 0:
                board[r][c] = 1
    # 2번 선거구 설정
    for r in range(1, x + d2 + 1):
        for c in range(y + 1, n + 1):
            if board[r][c] == 0:
                board[r][c] = 2
    # 3번 선거구 설정
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if board[r][c] == 0:
                board[r][c] = 3
    # 4번 선거구 설정
    for r in range(x + d2 + 1, n + 1):
        for c in range(y - d1 + d2, n + 1):
            if board[r][c] == 0:
                board[r][c] = 4
    return board

# 인구가 가장 많은 선거구와 가장 적은 선거구의 차 구하기
def get_gap(board, A, n):
    인구 = [0, 0, 0, 0, 0]
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            선거구 = board[x][y] - 1
            인구[선거구] += A[x - 1][y - 1]
    MAX = max(인구)
    MIN = min(인구)
    return MAX - MIN

# 재현시의 크기 N을 입력받기
n = int(input())

# 맵 입력받기
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# 결과
result = 100000

# 기준점, 경계 길이 구하기
for x in range(1, n - 1):
    for y in range(2, n):
        for d1 in range(1, y):
            for d2 in range(1, n - y + 1):
                # print(x, y, d1, d2)
                # print(d1 + d2, n - x)
                if d1 + d2 > n - x:
                    continue
                # 기준점, 길이가 모두 구해진 상태
                else:
                    board = get_map(n, x, y, d1, d2)
                    gap = get_gap(board, A, n)
                    result = min(result, gap)

print(result)
