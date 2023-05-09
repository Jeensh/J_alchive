from collections import deque
from copy import deepcopy

# 바이러스는 활성 / 비활성 상태가 있다
# 가장 처음에는 모든 바이러스가 비활성
# 활성 바이러스는 상하좌우 인접한 모든 빈칸으로 동시에 복제되며 1초가 걸림
# 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다

# 연구소는 n x n 크기
# 연구소는 빈칸, 벽, 바이러스로 이루어짐

# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함

count = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# comb
def comb(arr, n):
    result = []
    if len(arr) < n:
        return result
    if n == 1:
        for item in arr:
            result.append([item])
    elif n > 1:
        for i in range(len(arr) - (n - 1)):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

# 활성 바이러스 복제하기
# 복제가 진행된 경우 True 반환
# 진행되지 않은 경우 False 반환
def spread(board, n):
    global count
    flag = False
    visited = [[False] * n for i in range(n)]
    for x in range(n):
        for y in range(n):
            v = board[x][y]
            if v != '*' and v != '-' and v != 'b':
                if visited[x][y]:
                    continue
                count += 1
                print(count)
                visited[x][y] = True
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny]:
                            continue
                        # 퍼지는 곳이 빈칸인 경우
                        # 퍼지는 곳이 비활성 바이러스인 경우
                        if board[nx][ny] == '*' or board[nx][ny] == 'b':
                            board[nx][ny] = board[x][y] + 1
                            visited[nx][ny] = True
                            flag = True
    return flag


# 바이러스가 퍼지는 최소시간 구하기
# 빈칸이 있는 경우 -1 반환
def get_time(board, n):
    time = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'b':
                return -1
            elif board[x][y] == '-' or board[x][y] == '*':
                continue
            else:
                time = max(time, board[x][y])
    return time


########### 진행 ###########
# n, m 입력받기
n, m = map(int, input().split())

# 연구소의 상태 입력받기
# 0 : 빈칸, 1 : 벽, 2 : 바이러스를 놓을 수 있는 위치
proto_board = []
for i in range(n):
    proto_board.append(list(map(int, input().split())))

# 바이러스가 놓일 수 있는 위치 찾기
바이러스 = []
for x in range(n):
    for y in range(n):
        if proto_board[x][y] == 2:
            proto_board[x][y] = '*'
            바이러스.append((x, y))
        elif proto_board[x][y] == 1:
            proto_board[x][y] = '-'
        else:
            proto_board[x][y] = 'b'

# 바이러스가 놓일 수 있는 위치 중 바이러스 개수 만큼 뽑기
cases = comb(바이러스, m)

# 각 케이스 마다 확인하여 최저 시간을 찾기
result = 10000
for case in cases:
    # 바이러스 활성 세팅
    board = []
    for line in proto_board:
        board.append(line[:])

    for x, y in case:
        board[x][y] = 0

    if get_time(board, n) != -1:
        result = 0
        break

    while 1:
        # 복제 진행
        happend = spread(board, n)
        # 복제가 진행된 경우
        if happend:
            # 결과가 -1이 아닌경우
            time = get_time(board, n)
            if time != -1:
                result = min(result, get_time(board, n))
                break
        # 복제가 진행되지 않은 경우
        else:
            time = get_time(board, n)
            if time == -1:
                break
            else:
                result = min(result, get_time(board, n))
                break
if result == 10000:
    print(-1)
else:
    print(result)