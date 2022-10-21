# 3x3x3 큐브 정육면체
# 각 면을 양방향으로 90도 만큼 돌릴 수 있도록 만들어져 있다
# 회전을 마친 후에는, 다른 면을 돌릴 수 있다

# 루빅스 큐브가 모두 풀린 상태에서 시작
# 윗면 : 흰색
# 아랫면 : 노란색
# 앞면 : 빨간색
# 뒷면 : 오렌지색
# 왼쪽면 : 초록색
# 오른쪽면 : 파란색

# 루빅스 큐브를 돌린 방법이 순서대로 주어짐
# 모두 돌린 이후 가장 윗면의 색상을 구하는 프로그램 작성

# 각 모서리 옆
# 위 왼 아래 오른
위 = [(0, 0), (0, 1), (0, 2)]
왼 = [(0, 0), (1, 0), (2, 0)]
아래 = [(2, 0), (2, 1), (2, 2)]
오른 = [(0, 2), (1, 2), (2, 2)]


# 큐브 옆 면 갱신
def side_spin(step, cube):
    side = step[0]
    d = step[1]
    tmp = [[], [], [], []]
    if d == '+':
        # 위
        if side == 1:
            for i in range(3):
        # 아래
        elif side = 2:
        # 앞
        elif side = 3:
        # 뒤
        elif side = 4:
        # 왼
        elif side = 5:
        # 오른
        elif side = 6:

    elif d == '-':
        for i in range(3):
            side_spin((side, '+'), cube)


# 큐브 면 돌리기
def spin(step, cube):
    side = step[0]
    d = step[1]
    tmp = [[0] * 3 for i in range(3)]
    # 시계 방향으로 돌리는 경우
    if d == '+':
        for x in range(3):
            for y in range(3):
                # 가운데는 그대로
                if x == 1 and y == 1:
                    tmp[1][1] = cube[side][1][1]
                # 각 모서리
                elif x == 0 and y == 0:
                    tmp[0][2] = cube[side][0][0]
                elif x == 0 and y == 2:
                    tmp[2][2] = cube[side][0][2]
                elif x == 2 and y == 2:
                    tmp[2][0] = cube[side][2][2]
                elif x == 2 and y == 0:
                    tmp[0][0] = cube[side][2][0]
                # 모서리 중간
                elif x == 0 and y == 1:
                    tmp[1][2] = cube[side][0][1]
                elif x == 1 and y == 2:
                    tmp[2][1] = cube[side][1][2]
                elif x == 2 and y == 1:
                    tmp[1][0] = cube[side][2][1]
                elif x == 1 and y == 0:
                    tmp[0][1] = cube[side][1][0]
    # 반 시계 방향으로 돌리는 경우
    elif d == '-':
        for x in range(3):
            for y in range(3):
                # 가운데는 그대로
                if x == 1 and y == 1:
                    tmp[1][1] = cube[side][1][1]
                # 각 모서리
                elif x == 0 and y == 0:
                    tmp[2][0] = cube[side][0][0]
                elif x == 0 and y == 2:
                    tmp[0][0] = cube[side][0][2]
                elif x == 2 and y == 2:
                    tmp[0][2] = cube[side][2][2]
                elif x == 2 and y == 0:
                    tmp[2][2] = cube[side][2][0]
                # 모서리 중간
                elif x == 0 and y == 1:
                    tmp[1][0] = cube[side][0][1]
                elif x == 1 and y == 2:
                    tmp[0][1] = cube[side][1][2]
                elif x == 2 and y == 1:
                    tmp[1][2] = cube[side][2][1]
                elif x == 1 and y == 0:
                    tmp[2][1] = cube[side][1][0]
    cube[side] = tmp
    side_spin(step, cube)

# 테스트 케이스 개수
tc = int(input())

for _ in range(tc):
    # 큐브를 돌린 횟수 n
    n = int(input())
    # 큐브를 돌린 방법
    # + : 시계방향, - : 반시계 방향 (그 면을 바라봤을 때 기준)
    step = list(input().split())

    # 큐브 만들기
    # 순서 : 위, 아래, 앞, 뒷, 왼, 오른
    cube = [[],
            [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],]

    # 큐브 돌리기
    for s in step:
        side = s[0]
        d = s[1]
        if side == 'U':
            side = 1
        elif side == 'D':
            side = 2
        elif side == 'F':
            side = 3
        elif side == 'B':
            side = 4
        elif side == 'L':
            side = 5
        elif side == 'R':
            side = 6
        spin((side, d), cube)

    for i in range(3):
        for j in range(3):
            print(cube[1][i][j], end = '')
        print()