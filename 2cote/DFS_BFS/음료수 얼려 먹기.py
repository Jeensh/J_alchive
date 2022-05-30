# 세로길이 N과 가로길이 M 입력받기
N, M = map(int, input().split())

# 얼음 틀 형태 입력받기
board = []
for i in range(N):
    tmp = input()
    tmp_l = []
    for i in range(len(tmp)):
        tmp_l.append(int(tmp[i]))
    board.append(tmp_l)

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 방문완료된 곳 체크하는 리스트(전체)
visited = []

# 범위를 벗어나는 곳인지 확인
def check (v, d):
    global N, M
    if v[0] + d[0] < 0 or v[0] + d[0] > N - 1:
        return False
    elif v[1] + d[1] < 0 or v[1] + d[1] > M - 1:
        return False
    return True

# 현재 노드와 연결되어 있는 노드 전부 방문처리
def dfs(v):
    global board
    board[v[0]][v[1]] = 1
    for d in directions:
        if check(v, d) and board[v[0] + d[0]][v[1] + d[1]] == 0:
            dfs((v[0] + d[0], v[1] + d[1]))

# 문제 풀이
def solve():
    count = 0
    global N, M, board
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                dfs((row, col))
                count += 1
    return count

# 결과 출력
print(solve())