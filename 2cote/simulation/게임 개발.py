from distutils.spawn import spawn
from posixpath import split
import sys
input = sys.stdin.readline

# 방향 옵션 - 북 서 남 동
directions_id = [0, 3, 2, 1]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 행 / 열 크기 입력받기
N, M = map(int, input().split())

# 게임 캐릭터의 시작 지점과 방향 입력받기
a, b, c = map(int, input().split())
pos = [a, b, directions[c]]

# 맵 정보 입력받기
board = []
for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)

# 방문 여부 확인 지도 생성
visited = [[0 for i in range(M)] for j in range(N)]
for r in range(M):
    for c in range(N):
        if board[r][c] == 1:
            visited[r][c] = 1
visited[pos[0]][pos[1]] = 1

# 캐릭터의 움직임
'''
- 반시계 방향으로 차례대로 갈 곳을 정함
    - 향한 방향에 아직 가보지 않은 칸이 있다면 해당 방향으로 1칸 이동
        - 해당 방향에 아직 가보지 않은 칸이 없다면 다시 반시계 방향 회전
    - 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는
        - 방향 찾기 위해 회전하기 전 방향을 기준으로 바라보는 방향을 유지한 채로 한칸 뒤로 이동
        - 이때, 만약 뒤쪽 방향이 바다인 칸이라면 움직임을 멈춘다
'''
# 향한 방향에 아직 가보지 않은 칸이 있는지 확인하는 함수
def there_is_space_to_move():
    global pos, visited
    pos_tmp = (pos[0], pos[1], pos[2])
    while((pos_tmp[0] > 0 and pos_tmp[0] < N) and (pos_tmp[1] > 0 and pos_tmp[1] < M)):
        if visited[pos_tmp[0]][pos_tmp[1]] == 0:
            if visited[pos[0] + pos[2][0]][pos[1] + pos[2][1]] == 0:
                return True
        pos_tmp = (pos_tmp[0] + pos_tmp[2][0], pos_tmp[1] + pos_tmp[2][1], pos_tmp[2])
    return False

# 방문한 카운터 수 체크 변수
count = 1
def move():
    global count, pos, board, directions, visited
    for i in range(4):
        # 반시계 방향 전환
        pos = [pos[0], pos[1], directions[(directions.index(pos[2]) + 1) % 4]]
        to_go = [pos[0] + pos[2][0], pos[1] + pos[2][1], pos[2]]
        # 향한 방향에 아직 가보지 않은 칸이 있고 육지라면 해당 방향으로 1칸 이동
        if (there_is_space_to_move()):
            pos = to_go
            visited[pos[0]][pos[1]] = 1
            count += 1
            return True
    # 네방향 모두 이미 가본칸이거나 바다로 되어있는 경우
    # 뒤쪽이 바다라면 움직임 멈춤
    back_direction = directions[(directions.index(pos[2]) + 2) % 4]
    if board[pos[0] + back_direction[0]][pos[1] + back_direction[1]] == 1:
        return False
    # 뒤쪽이 바다가 아니라면 그대로 뒤로 이동(방향 전환 x)
    pos = [pos[0] + back_direction[0], pos[1] + back_direction[1], pos[2]]
    return True

while(1):
    if not move():
        break

print(count)