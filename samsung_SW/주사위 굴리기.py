# 지도의 세로 크기 N, 가로 크기 M, 주사위를 놓은 곳의 좌표 x,y , 명령의 개수 K 입력받기
N, M, x, y, K = map(int, input().split())

# 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어짐
map1 = []
for i in range(N):
    map1.append(list(map(int, input().split())))

# 명령 입력받기(동 : 1, 서 : 2, 북 : 3, 남 : 4)
directions = list(map(int, input().split()))

# 주사위 위치 초기화
pos = (x, y)

# 주사위 상태 초기화
dice_updown = [0, 0, 0, 0]
dice_leftright = [0, 0, 0, 0]

# 오른쪽으로 굴리기(1)
def roll_right(map, dice_updown, dice_leftright):
    global pos
    # 주사위 위치 변경
    tmp = pos
    pos = (pos[0], pos[1] + 1)

    # 맵을 벗어나는지 확인
    if (pos[0] > N - 1 or pos[0] < 0) or (pos[1] > M - 1 or pos[1] < 0):
        pos = tmp
        return -1

    # 주사위 상태 변경
    # 가로 상태
    tmp = dice_leftright[0]
    del(dice_leftright[0])
    dice_leftright.append(tmp)
    # 세로 상태
    dice_updown[0] = dice_leftright[0]
    dice_updown[2] = dice_leftright[2]

    # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사
    if map[pos[0]][pos[1]] == 0:
        map[pos[0]][pos[1]] = dice_updown[2]
    else:	# 아닌 경우에는 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸에 쓰여있는 수는 0이됨
        dice_updown[2] = map[pos[0]][pos[1]]
        dice_leftright[2] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = 0

    return 1

# 왼쪽으로 굴리기(2)
def roll_left(map, dice_updown, dice_leftright):
    global pos
    # 주사위 위치 변경
    tmp = pos
    pos = (pos[0], pos[1] - 1)

    # 맵을 벗어나는지 확인
    if (pos[0] > N - 1 or pos[0] < 0) or (pos[1] > M - 1 or pos[1] < 0):
        pos = tmp
        return -1

    # 주사위 상태 변경
    # 가로 상태
    tmp = dice_leftright[3]
    del(dice_leftright[3])
    dice_leftright.insert(0, tmp)
    # 세로 상태
    dice_updown[0] = dice_leftright[0]
    dice_updown[2] = dice_leftright[2]

    # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사
    if map[pos[0]][pos[1]] == 0:
        map[pos[0]][pos[1]] = dice_updown[2]
    else:	# 아닌 경우에는 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸에 쓰여있는 수는 0이됨
        dice_updown[2] = map[pos[0]][pos[1]]
        dice_leftright[2] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = 0

    return 1

# 위쪽으로 굴리기(3)
def roll_up(map, dice_updown, dice_leftright):
    global pos
    # 주사위 위치 변경
    tmp = pos
    pos = (pos[0] - 1, pos[1])

    # 맵을 벗어나는지 확인
    if (pos[0] > N - 1 or pos[0] < 0) or (pos[1] > M - 1 or pos[1] < 0):
        pos = tmp
        return -1

    # 주사위 상태 변경
    # 가로 상태
    tmp = dice_updown[3]
    del(dice_updown[3])
    dice_updown.insert(0, tmp)
    # 세로 상태
    dice_leftright[0] = dice_updown[0]
    dice_leftright[2] = dice_updown[2]

    # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사
    if map[pos[0]][pos[1]] == 0:
        map[pos[0]][pos[1]] = dice_updown[2]
    else:	# 아닌 경우에는 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸에 쓰여있는 수는 0이됨
        dice_updown[2] = map[pos[0]][pos[1]]
        dice_leftright[2] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = 0

    return 1

# 아래쪽으로 굴리기(4)
def roll_down(map, dice_updown, dice_leftright):
    global pos
    # 주사위 위치 변경
    tmp = pos
    pos = (pos[0] + 1, pos[1])

	# 맵을 벗어나는지 확인
    if (pos[0] > N - 1 or pos[0] < 0) or (pos[1] > M - 1 or pos[1] < 0):
        pos = tmp
        return -1

    # 주사위 상태 변경
    # 가로 상태
    tmp = dice_updown[0]
    del(dice_updown[0])
    dice_updown.append(tmp)
    # 세로 상태
    dice_leftright[0] = dice_updown[0]
    dice_leftright[2] = dice_updown[2]

    # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사
    if map[pos[0]][pos[1]] == 0:
        map[pos[0]][pos[1]] = dice_updown[2]
    else:	# 아닌 경우에는 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸에 쓰여있는 수는 0이됨
        dice_updown[2] = map[pos[0]][pos[1]]
        dice_leftright[2] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = 0

    return 1

for d in directions:
    if d == 1:
        tmp = roll_right(map1, dice_updown, dice_leftright)
    elif d == 2:
        tmp = roll_left(map1, dice_updown, dice_leftright)
    elif d == 3:
        tmp = roll_up(map1, dice_updown, dice_leftright)
    elif d == 4:
        tmp = roll_down(map1, dice_updown, dice_leftright)
    if tmp == -1:
        continue
    # print('-------------')
    # print(pos)
    # print(d)
    # print(dice_leftright)
    # print(dice_updown)
    # print('-------------')
    print(dice_leftright[0])