from collections import deque

# 공간의 크기 N 입력받기
N = int(input())

# 공간의 상태 입력받기
# 0 : 빈칸
# 1, 2, 3, 4, 5, 6 : 칸에 있는 물고기 크기
# 9 : 아기 상어의 위치
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 상어크기
s_size = 2
ate = 0

result = 0

def check_avail(board, s_size, visited, x, y):
    global N
    if x < 0 or x > N - 1:
        return False
    elif y < 0 or y > N - 1:
        return False
    elif board[x][y] > s_size:
        return False
    elif (x, y) in visited:
        return False
    return True

def calc(board, s_size):
    global N
    # 상어 찾기
    pos = ()
    can_eat = deque()
    min_length = 100000
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                pos = (0, i, j)
                board[i][j] = 0
    visited = [(pos[1], pos[2])]
    queue = deque([pos])

    while(queue):
        pos = queue.pop()
        if board[pos[1]][pos[2]] != 0 and board[pos[1]][pos[2]] < s_size:
            if pos[0] > min_length:
                break
            can_eat.append(pos)
            min_length = min(min_length, pos[0])
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (check_avail(board, s_size, visited, pos[1] + x, pos[2] + y)):
                visited.append((pos[1] + x, pos[2] + y))
                queue.appendleft((pos[0] + 1, pos[1] + x, pos[2] + y))
    if can_eat:
        tmp = []
        for f in can_eat:
            tmp.append((f[1] * N) + f[2])
        tmp.sort()
        x = tmp[0] // N
        y = tmp[0] % N
        return can_eat[0][0], x, y
    else:
        return 0, 0, 0

while(1):
    ret, x, y = calc(board, s_size)
    if ret == 0:
        break
    board[x][y] = 9
    ate += 1
    if ate == s_size:
        s_size += 1
        ate = 0
    result += ret

print(result)