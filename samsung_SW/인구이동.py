import sys
sys.setrecursionlimit(10000)
# nxn 크기의 땅
# 각 원소의 값은 해당 나라에 사는 인구

# 인구이동은 하루동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속
#   - 국경선을 공유하는 두 나라의 인구차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 하루 동안 연다
#   - 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면 인구 이동 시작
#   - 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안 연합이라 함
#   - 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수)/(연합을 이루고 있는 칸의 개수)가 된다, 편의상 소수점은 버린다
#   - 연합을 해체하고 모든 국경선을 닫는다

# 인구 이동이 며칠동안 발생하는지 구하는 프로그램 작성

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인구 차이 확인 함수
def check_gap(board, x, y, x2, y2, l, r):
    gap = abs(board[x][y] - board[x2][y2])
    if gap >= l and gap <= r:
        return True
    else:
        return False

# 연합 인구 이동 진행 함수
def move(board, union):
    total = 0
    n = 0
    for country in union:
        n += 1
        x, y = country
        total += board[x][y]
    result = total // n
    for country in union:
        x, y = country
        board[x][y] = result

# dfs로 연합 찾기
def dfs(union_map, x, y, n, union, count):
    union_map[x][y] = 0
    union.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if union_map[nx][ny] == count:
                dfs(union_map, nx, ny, n, union, count)

# dfs로 연합 맺기
def dfs2(union_map, x, y, n, l, r, count):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if union_map[nx][ny] == count:
                continue
            if check_gap(board, x, y, nx, ny, l, r):
                union_map[x][y] = count
                union_map[nx][ny] = count
                dfs2(union_map, nx, ny, n, l, r, count)


# n, l, r 입력받기
n, l, r = map(int, input().split())
# 각 나라의 인구수 입력받기
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

union_map = [[0] * n for i in range(n)]

day = 0
while 1:
    flag = True
    count = 1
    # 연합 맺기 진행
    for x in range(n):
        for y in range(n):
            dfs2(union_map, x, y, n, l, r, count)
            count += 1
    # for i in union_map:
    #                 print(i)
    # 연합 확인하여 인구 이동 진행
    for x in range(n):
        for y in range(n):
            if union_map[x][y] != 0:
                flag = False
                union = []
                # print('---------------')
                # for i in board:
                    # print(i)
                # for i in union_map:
                #     print(i)
                dfs(union_map, x, y, n, union, union_map[x][y])
                # print('--')
                # for i in union_map:
                #     print(i)
                move(board, union)
    if flag:
        break
    day += 1

# for i in board:
#     print(i)
print(day)