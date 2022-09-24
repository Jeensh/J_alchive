# 상하좌우
fx = [-1, 1, 0 , 0]
fy = [0, 0, -1, 1]

# 자연수 n, k 입력받기
n, k = map(int, input().split())

# 시험관의 정보 입력받기
board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

# s, x, y 입력받기
s, x, y = map(int, input().split())

# 바이러스의 위치를 저장할 테이블 만들기
virus = [[] for i in range(k + 1)]

# 바이러스 초기 위치를 테이블에 저장하기
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virus_number = board[i][j]
            virus[virus_number].append((i, j))

# 1초의 시간을 흐르게 만들기
def spread(virus, board):
    for i in range(1, len(virus)):
        new_virus_pos = []
        for pos in virus[i]:
            for j in range(4):
                nx = pos[0] + fx[j]
                ny = pos[1] + fy[j]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if board[nx][ny] == 0:
                        board[nx][ny] = i
                        new_virus_pos.append((nx, ny))
        virus[i] = new_virus_pos

# s초의 시간을 흐르게 만들기
for i in range(s):
    spread(virus, board)

# (x, y)에 존재하는  바이러스 종류 출력
print(board[x - 1][y - 1])