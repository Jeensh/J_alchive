from collections import deque
import sndhdr

# 보드의 크기 N 입력받기
N = int(input())

# 사와의 개수 K 입력받기
K = int(input())

# 사과의 위치 입력받기 (행, 열)
apples = []
for i in range(K):
    a, b = map(int, input().split())
    apples.append((a, b))

# 뱀의 방향 변환 횟수 L 입력받기
L = int(input())

# 뱀의 방향 변환정보, 정수 X와 문자 C 입력받기
# 게임시작 후 X초가 끝난 뒤 왼쪽(L), 또는 오른쪽(D)으로 90도 방향 회전한다는 뜻
actions = []
for i in range(L):
    X, C = input().split()
    actions.append((int(X), C))

# 방향 순서 리스트 만들기
d_list = ['right', 'down', 'left', 'up']

# 보드 만들기
board = [[0 for i in range(N + 2)] for j in range(N + 2)]

# 벽 만들기(-1)
for i in range(N + 2):
    for j in range(N + 2):
        if i == 0 or j == 0 or i == N + 1 or j == N + 1:
            board[i][j] = -1

# 뱀 상태 변수 초기화(머리 방향) - up, down, left, right
snake = deque()
snake.append((1,1))
status = 'right'

# 뱀 머리 이동
def move(snake, status):
    if status == 'right':
        if (snake[0][0], snake[0][1] + 1) in snake:
            return -1
        snake.appendleft((snake[0][0], snake[0][1] + 1))
    elif status == 'left':
        if (snake[0][0], snake[0][1] - 1) in snake:
            return -1
        snake.appendleft((snake[0][0], snake[0][1] - 1))
    elif status == 'up':
        if (snake[0][0] - 1, snake[0][1]) in snake:
            return -1
        snake.appendleft((snake[0][0] - 1, snake[0][1]))
    elif status == 'down':
        if (snake[0][0] + 1, snake[0][1]) in snake:
            return -1
        snake.appendleft((snake[0][0] + 1, snake[0][1]))
    return 1

count = 0
while(1):
    count += 1
    # 뱀 머리 이동
    tmp = move(snake, status)
    # 머리가 벽에 부딛혔을 시 사망
    if board[snake[0][0]][snake[0][1]] == -1:
        break
    # 머리가 꼬리에 부딛혔을 시 사망
    if tmp == -1:
        break
    # 머리에 사과가 있을 시 먹음, 그리고 꼬리 줄이지 않음
    if snake[0] in apples:
        apples.remove(snake[0])
    else:	# 머리에 사과가 없을 경우에는 꼬리 줄임
        snake.pop()
    # 머리 방향 변경 있는지 확인 후 적용
    if actions and count == actions[0][0]:
        if actions[0][1] == 'D': # 오른쪽으로 90도
            status = d_list[(d_list.index(status) + 1) % 4]
        elif actions[0][1] == 'L': # 왼쪽으로 90도
            if d_list.index(status) == 0:
                status = d_list[3]
            else:
                status = d_list[d_list.index(status) - 1]
        actions.remove(actions[0])

print(count)