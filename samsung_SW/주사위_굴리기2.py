from collections import deque
# 크기 n x m 인 지도
# (1, 1) 부터 시작
# 주사위 각 면에는 1 ~ 6 정수가 있음

# 주사위는 지도위에 윗면이 1이고 동쪽이 3인 상태로 놓여져 있음
# 놓여진 곳의 좌표는 (1, 1)
# 지도의 각 칸에도 정수가 하나씩 있음
# 가장 처음에 주사위의 이동방향은 동쪽

# 주사위의 이동 한번은 다음과 같다
#   1. 주사위가 이동 방향으로 한 칸 굴러간다, 만약 이동 방향에 칸이 없다면 반대로 한칸 굴러감
#   2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득
#   3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동방향 결정
#       - A > B 인 경우 이동 방향을 90도 시계 방향으로 회전시킴
#       - A < B 인 경우 이동 방향을 90도 반시계 방향으로 회전
#       - A = B 인 경우 이동방향 변화 없음

# 칸 (x,y) 에 대한 점수는 다음과 같이 구할 수 있다
# (x, y)에 있는 정수를 B라고 했을 때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다
# 이떄 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다
# 여기서 점수는 B와 C를 곱한 값이다
# 점수를 bfs로 구하면 될듯

# 보드의 크기와 각 칸에 있는 정수, 주사위의 이동횟수 k
# 점수의 합 구하기

# 주사위 가로, 세로
# 동쪽, 북쪽 방향
dice_h = [6, 3, 1, 4]
dice_v = [6, 2, 1, 5]

# 방향 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 반대 방향
# 서 북 동 남
reverce_d = [2, 3, 0, 1]

# 주사위 굴리기
# 동, 서, 남, 북
def roll(d, dice_h, dice_v):
    # 동
    if d == 0:
        tmp = dice_h[0]
        del dice_h[0]
        dice_h.append(tmp)
        dice_v[0] = dice_h[0]
        dice_v[2] = dice_h[2]
    # 서
    elif d == 2:
        tmp = dice_h[3]
        dice_h.pop()
        dice_h.insert(0, tmp)
        dice_v[0] = dice_h[0]
        dice_v[2] = dice_h[2]
    # 남
    elif d == 1:
        tmp = dice_v[3]
        dice_v.pop()
        dice_v.insert(0, tmp)
        dice_h[0] = dice_v[0]
        dice_h[2] = dice_v[2]
    # 북
    elif d == 3:
        tmp = dice_v[0]
        del dice_v[0]
        dice_v.append(tmp)
        dice_h[0] = dice_v[0]
        dice_h[2] = dice_v[2]

# 방향 변경하기
def set_d(board, x, y, d, dice_h, dice_v):
    A = dice_v[0]
    B = board[x][y]
    if A > B:
        return (d + 1) % 4
    elif A < B:
        if d == 0:
            return 3
        else:
            return d - 1
    else:
        return d

# 점수 획득하기
def get_score(board, x, y, n, m):
    visited = [[False] * m for i in range(n)]
    q = deque()
    std = board[x][y]
    total = 0
    q.appendleft((x, y))
    visited[x][y] = True
    while q:
        x, y = q.pop()
        total += std
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == std:
                    visited[nx][ny] = True
                    q.appendleft((nx, ny))
    return total


# n, m, k 입력받기
n, m, k = map(int, input().split())

# 지도 입력받기
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 진행
turn = 0
result = 0
x = 0
y = 0
d = 0
while turn < k:
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        d = reverce_d[d]
    x = x + dx[d]
    y = y + dy[d]
    roll(d, dice_h, dice_v)
    result += get_score(board, x, y, n, m)
    d = set_d(board, x, y, d, dice_h, dice_v)
    turn += 1
print(result)

# 동 남 서 북