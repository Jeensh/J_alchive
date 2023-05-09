# 드래곤 커브는 3가지 속성
#   1. 시작점
#   2. 시작 방향
#   3. 세대

# 0세대 드래곤 커브
# 길이가 1

# k 세대 드래곤 커브는 k-1세대 드래곤 커브를 끝점을 기준으로
# 90도 시계방향 회전시킨 다음 그것을 끝점에 붙인 것

# 크기가 100 x 100인 격자위에 드래곤 커브가 n개
# 이때, 크기가 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수는?

# 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

왼쪽위x = [0, -1, -1]
왼쪽위y = [-1, 0, -1]
오른쪽위x = [0, -1,-1]
오른쪽위y = [1, 1, 0]
왼쪽아래x = [0, 1, 1]
왼쪽아래y = [-1, 0, -1]
오른쪽아래x = [0, 1, 1]
오른쪽아래y = [1, 0, 1]

# 정사각형 개수 확인
def get_count(board):
    count = 0
    for i in range(1, 100):
        for j in range(1, 100):
            # 왼쪽위 오른쪽위 완쪽아래 오른쪽 아래
            if board[i][j] == 1:
                if i == 1 and j == 1:
                    for t in range(3):
                        nx = i + 왼쪽위x[t]
                        ny = j + 왼쪽위y[t]
                        if board[nx][ny] == 1:
                            if t == 2:
                                count += 1
                            continue
                        break
                if i == 1:
                    for t in range(3):
                        nx = i + 오른쪽위x[t]
                        ny = j + 오른쪽위y[t]
                        if board[nx][ny] == 1:
                            if t == 2:
                                count += 1
                            continue
                        break
                if i != 1 and j == 1:
                    for t in range(3):
                        nx = i + 왼쪽아래x[t]
                        ny = j + 왼쪽아래y[t]
                        if board[nx][ny] == 1:
                            if t == 2:
                                count += 1
                            continue
                        break
                for t in range(3):
                    nx = i + 오른쪽아래x[t]
                    ny = j + 오른쪽아래y[t]
                    if board[nx][ny] == 1:
                        if t == 2:
                             count += 1
                        continue
                    break
    return count

# 드래곤 커브 위치 맵에 갱신하기
def curve(board, x, y, d, g):
    i = 1
    board[x][y] = 1
    nx = x + dx[d]
    ny = y + dy[d]
    board[nx][ny] = 1
    past = [d]
    while i <= g:
        tmp = []
        for di in past:
            di = (di + 1) % 4
            nx += dx[di]
            ny += dy[di]
            board[nx][ny] = 1
            tmp.append(di)
        tmp.reverse()
        past = tmp + past
        i += 1

# 드래곤 커브의 개수 n 입력받기
n = int(input())
# 드래곤 커브의 정보 입력받기
# x,y : 시작점, d : 시작 방향, g : 세대
dragons = []
for i in range(n):
    y, x, d, g = map(int, input().split())
    dragons.append((x, y, d, g))

# 맵 만들기
board = [[0] * 101 for i in range(101)]

for dragon in dragons:
    x, y, d, g = dragon
    curve(board, x, y, d, g)

# for i in board[:10]:
#     print(i[:10])

print(get_count(board))