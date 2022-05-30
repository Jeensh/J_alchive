from collections import deque

# 맵 세로 길이 N, 가로 길이 M 입력받기
N, M = map(int, input().split())

# 맵 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input())))

# 시작위치, 목적지 초기화
start = (0, 0)
goal = (N - 1, M - 1)

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 범위 벗어나는지 확인
def check(nv):
    if nv[0] < 0 or nv[0] > N - 1:
        return False
    elif nv[1] < 0 or nv[1] > M - 1:
        return False
    return True

# 시작위치 부터 시작하여 BFS로 가장 먼저 도착한 녀석 움직인 횟수 찾기
def solve():
    queue = deque([])
    # 시작위치와 연결된 노드 큐에 넣기
    board[start[0]][start[1]] = 0
    for d in directions:
        nv = (start[0] + d[0], start[1] + d[1], 2)
        if check(nv) and board[nv[0]][nv[1]] == 1:
            queue.append(nv)
    # 도착(or 갈곳이 없을)할 때까지 BFS 탐색
    while queue:
        v = queue.popleft()
        if v[0] == N - 1 and v[1] == M - 1:
            return v[2]
        board[v[0]][v[1]] = 0
        for d in directions:
            nv = (v[0] + d[0], v[1] + d[1], v[2] + 1)
            if check(nv) and board[nv[0]][nv[1]] == 1:
                queue.append(nv)
    return 0

# 결과 출력
print(solve())